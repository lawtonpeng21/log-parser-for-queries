import re
import os
import pandas as pd

class LogParser:
    def __init__(self, log_file_path, output_folder):
        self.log_file_path = log_file_path
        self.output_folder = output_folder
        self.log_files = self._get_log_files()

    def _get_log_files(self):
        if not os.path.exists(self.log_file_path):
            print("Folder does not exist")
            return []

        log_files = [file for file in os.listdir(self.log_file_path) if file.endswith(".txt")]
        return log_files

    def extract_information(self, keyword, timestamp_pattern, date_pattern):
        for file_name in self.log_files:
            file_path = os.path.join(self.log_file_path, file_name)
            with open(file_path, 'r', encoding="utf8") as file:
                lines = file.readlines()

            query_found = False
            timestamp_string = ""
            query_string = ""
            date_string = ""
            username = ""
            parsed_data = []

            for line in lines:
                if query_found:
                    if re.search(timestamp_pattern, line):
                        timestamp_string = re.findall(timestamp_pattern, line)[0]
                        parsed_entry = {"Timestamp": timestamp_string, "Date": date_string, "Username": username, "Query": query_string.strip()}
                        parsed_data.append(parsed_entry)
                        query_string = ""
                        query_found = False
                    else:
                        query_string += line.strip() + "\n"
                elif re.search(keyword, line) and re.search(timestamp_pattern, line):
                    if re.search(date_pattern, line):
                        date_string = re.findall(date_pattern, line)[0]
                    timestamp_string = re.findall(timestamp_pattern, line)[0]
                    query_found = True

                    # Extract username from the line
                    match = re.search(r'#(.+)', line)
                    if match:
                        username = match.group(1).strip()
                    else:
                        username = "Username not found"

            output_file_path = os.path.join(self.output_folder, file_name.replace(".txt", "_parsed.csv"))
            df = pd.DataFrame(parsed_data)
            df.to_csv(output_file_path, index=False)

            print(f"Parsed information saved to {output_file_path}")




