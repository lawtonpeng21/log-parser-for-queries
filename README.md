# log-parser-for-queries
Python version 3.11.4

Make sure both log_parser_main.py and log_parser_module.py are both installed in the same directory.

To use this program:
1. Folder Paths:
* Replace "C:/path/to/your/log/folder" with the actual path to the folder containing your log files.
* The program will create parsed log files in the "parsed_logs" folder on your desktop.
2. Customization:
* Modify the keyword, timestamp_pattern, and date_pattern to match the format of your log files.
3. Running the Program:
* Run the log_parser_main.py, and it will process the log files, extract information, including usernames after the '#' symbol. 
4. Output:
* Parsed log files will be generated in the "parsed_logs" folder on your desktop.
* Each parsed file will have a name like original_file_name_parsed.csv.

Make sure to have Python installed on your system and have the required modules such as pandas installed using pip install -r requirements.txt. 




