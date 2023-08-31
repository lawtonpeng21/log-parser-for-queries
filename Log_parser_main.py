# Imports necessary libraries
import os
from .log_parser_module import LogParser

# Defines the main function
def main():
    # Defines the path to the folder containing log files
    log_folder_path = r"C:\Users\m295939\Desktop\New folder"  # Replace with the actual folder path

    # Defines the output folder for parsed logs
    output_folder = os.path.join(os.path.expanduser("~"), "Desktop", "parsed_logs")

    # Creates the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Creates an instance of the LogParser class
    log_parser = LogParser(log_folder_path, output_folder)

    # Defines patterns and keywords for log extraction
    keyword = "-DEBUG in i.u.i.o.a.r.impl.QuestQueryProcessor - SPARQL query:"
    timestamp_pattern = r'\d{2}:\d{2}:\d{2}\.\d{3}'
    date_pattern = r'\d{4}-\d{2}-\d{2}'

    # Extracts information from log files using the LogParser instance
    log_parser.extract_information(keyword, timestamp_pattern, date_pattern)

# Checks if the script is being run directly
if __name__ == "__main__":
    # Calls the main function to start the log parsing process
    main()
