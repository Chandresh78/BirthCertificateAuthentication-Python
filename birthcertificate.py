import os
import re

def find_pattern_in_text(text, pattern):
    matches = re.findall(pattern, text)
    return matches

def process_file(file_path, search_pattern):
    if os.path.exists(file_path):
        with open(file_path, 'r') as txt_file:
            text = txt_file.read()

        found_patterns = find_pattern_in_text(text, search_pattern)
        if found_patterns:
            output_statement = f"This {os.path.basename(file_path)} contains the pattern(s):"
            for pattern in found_patterns:
                output_statement += f"\n{pattern}"
            return output_statement
        else:
            return f"No '{search_pattern}' pattern found in the file."
    else:
        return f"The file {os.path.basename(file_path)} does not exist."

input_file_path = input("Enter the path to the text file: ")
search_pattern = "This Birth Certificate document dated 20 July 2005"

result = process_file(input_file_path, search_pattern)
print(result)
