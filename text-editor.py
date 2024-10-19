
def open_file(file_path):
    # this function opens a file at the given file_path in read mode ('r').
    # If successful, it reads all lines from the file and returns them as a list of strings.
    try: 
        with open(file_path, 'r') as file:
            return file.readlines()
    # If the file not found, it handles the exception and print error message.
    except FileNotFoundError:
        print("File not found!")
        return [] # Returns an empty list if the file doesnt exist.
    
def save_file(file_path, content):
    # This funtion opens a file at the given file_path in write mode ('w').
    # It writes all the content from the 'content' list into the file.
    with open(file_path, 'w') as file:
        file.writelines(content) # Writes each element of the content list as a new line in the file.
    print(f"File saved: {file_path}") # Confirms that the file was saved succesfully.
    
def display_content(content):
    # This function displays the content of the file with the line numbers.
    # It loops through the 'content' list and prints each line.
    for line_number, line in enumerate(content, 1):
        print(f"{line_number}: {line}", end='') # Prints each line with its line number.
        
# Example usage
file_path = input("Enter the file name to open: ") # Prompts the user to input the file name.
content = open_file(file_path) # Calls the open_file function and assigns the result (file content) to 'content'.

if content:
    display_content(content) # If the file has content, it is displayed line by line.
    
    # Allow editing
    user_input = input("\nDo you want to edit this file? (y/n): ") # Asks user if they want to edit the file.
    if user_input.lower() == 'y': # If the user says 'yes' (in any case, lower or uppercase):
        new_content = [] # Initializes an empty list to store new content.
        print("Enter new content(type 'SAVE' to save and exit): ") # Instruction to the user on how to finish input.
        while True:
            line = input() # Continuosly prompts user to input new lines of text.
            if line.upper() == "SAVE": # If user types 'SAVE', it breaks the loop to stop adding content.
                save_file(file_path, new_content) # Calls the save_file function to write the new content to the file.
                break # Exits the loop after saving.
            new_content.append(line + '\n') # Adds each new line to the 'new_content' list, ensuring a new line character.