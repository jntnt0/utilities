import os

def read_files_in_src(directory, log_file=None):
    """
    Walk through the directory and read all files in 'src' subdirectories.
    """
    if log_file:
        log = open(log_file, 'w')
    
    for root, dirs, files in os.walk(directory):
        if 'src' in root:
            for file in files:
                if file.endswith('.py'):  # Only read .py files
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            file_header = f"Reading file: {file_path}\n" + "-"*60 + "\n"
                            file_content = f.read()
                            file_separator = "\n" + "-"*60 + "\n\n"
                            
                            print(file_header)
                            print(file_content)
                            print(file_separator)
                            
                            if log_file:
                                log.write(file_header)
                                log.write(file_content)
                                log.write(file_separator)
                    except Exception as e:
                        error_message = f"Failed to read file: {file_path}. Error: {e}\n"
                        print(error_message)
                        if log_file:
                            log.write(error_message)
    
    if log_file:
        log.close()

# Specify the root directory here
root_directory = r"C:\Users\lunch#\Documents\GitHub\PCAP_Analysis_Features\src"
# Optionally, specify a log file
log_file_path = r"C:\logs\read_files_log.txt"
read_files_in_src(root_directory, log_file=log_file_path)
