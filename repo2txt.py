import os
import glob
import re

def extract_text_from_python_files(directory):
    file_paths = glob.glob(os.path.join(directory, '*.py'))
    extracted_text = []

    for file_path in file_paths:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

            # Remove comments (single-line and multi-line)
            content = re.sub(r'#.*?\n', '', content)  # Remove single-line comments
            content = re.sub(r'""".*?"""', '', content, flags=re.DOTALL)  # Remove multi-line comments

            # Extract function and variable names
            function_names = re.findall(r'def\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\(', content)
            variable_names = re.findall(r'\b([a-zA-Z_][a-zA-Z0-9_]*)\s*=', content)

            # Combine extracted text elements
            extracted_text.append({
                'file_name': os.path.basename(file_path),
                'content': content,
                'function_names': function_names,
                'variable_names': variable_names
            })

    return extracted_text

if __name__ == "__main__":
    directory = r'C:\Users\lunch#\Documents\GitHub\PCAP_Enumeration'  # Replace with your repository directory path
    extracted_text = extract_text_from_python_files(directory)

    # Example: Saving extracted text to a JSON file
    import json

    output_file = 'extracted_text.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(extracted_text, f, ensure_ascii=False, indent=4)

    print(f"Extracted text saved to {output_file}")

