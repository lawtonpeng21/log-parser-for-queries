import os
import sys
from log_parser_module import LogParser  # Import LogParser directly

# Add the directory containing log_parser_module.py to the Python path
module_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(module_dir)

def main():
    log_folder_path = r"C:\Users\m295939\Desktop\New folder"  # Replace with the actual folder path
    output_folder = os.path.join(os.path.expanduser("~"), "Desktop", "parsed_logs")

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    log_parser = LogParser(log_folder_path, output_folder)

    keyword = "-DEBUG in i.u.i.o.a.r.impl.QuestQueryProcessor - SPARQL query:"
    timestamp_pattern = r'\d{2}:\d{2}:\d{2}\.\d{3}'
    date_pattern = r'\d{4}-\d{2}-\d{2}'

    log_parser.extract_information(keyword, timestamp_pattern, date_pattern)

if __name__ == "__main__":
    main()

