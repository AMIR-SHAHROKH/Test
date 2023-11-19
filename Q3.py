# import ast

# def check_syntax_errors(file_path):
#     try:
#         with open(file_path, 'r') as file:
#             python_code = file.read()
#             tree = ast.parse(python_code)
#             print(f"No syntax errors found in '{file_path}'")
#             return 0  # Return 0 to indicate no syntax errors
#     except FileNotFoundError:
#         print(f"Error: File '{file_path}' not found.")
#         return -1  # Return -1 for file not found error
#     except SyntaxError as e:
#         print(f"Syntax error in '{file_path}':")
#         print(f"Error message: {e.msg}")
#         print(f"Line number: {e.lineno}")
#         return e.lineno  # Return the line number where the syntax error occurred
#     except Exception as ex:
#         print(f"An error occurred while processing '{file_path}': {ex}")
#         return -2  # Return -2 for other unexpected errors

# if __name__ == "__main__":
#     file_path = input("Enter the path to the Python file to check: ")
#     error_count = check_syntax_errors(file_path)
    
#     if error_count == 0:
#         print("No syntax errors found.")
#     elif error_count == -1:
#         print("File not found.")
#     elif error_count == -2:
#         print("Unexpected error occurred.")
#     else:
#         print(f"{error_count} syntax error(s) found.")
def check_text_syntax(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            lines = text.split('\n')

            error_count = 0
            for i, line in enumerate(lines):
                # Check for basic syntax issues (e.g., missing punctuation at the end of sentences)
                if line.strip() and not line.endswith('.') and not line.endswith('!') and not line.endswith('?'):
                    print(f"Potential syntax issue in line {i + 1}: Missing punctuation at the end of the sentence")
                    error_count += 1

                # You can add more checks based on your specific criteria here

            if error_count == 0:
                print("No potential syntax issues found.")
            else:
                print(f"Found {error_count} potential syntax issue(s) in '{file_path}'.")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")

if __name__ == "__main__":
    file_path = '.venv/HW2/text.txt'  # Replace with the path to your text file
    check_text_syntax(file_path)
