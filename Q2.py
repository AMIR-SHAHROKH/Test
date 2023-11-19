import re

def sed(file_input, file_output, pattern_string, replacement_string):
    try:
        with open(file_input, 'r') as input_file:
            content = input_file.read()
            
            # Perform pattern replacement
            updated_content = re.sub(pattern_string, replacement_string, content)
            
            # Write updated content to output file
            with open(file_output, 'w') as output_file:
                output_file.write(updated_content)
                print(f"Content of '{file_input}' has been updated and saved to '{file_output}'")
                
        # Display the content of the output file
        with open(file_output, 'r') as output_file:
            output_content = output_file.read()
            print(f"Content of '{file_output}':\n{output_content}")
            
    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'old_pattern' with 'new_pattern' in 'input.txt' and save to 'output.txt'
sed('input.txt', 'output.txt', r'old_pattern', r'new_pattern')
