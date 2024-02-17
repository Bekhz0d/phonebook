from extra_functions import read_from, append_to


# Function for reading contacts from a file
def read_contacts(file_name: str, page_size: int = 20) -> None:
    """
    This function reads a list of contacts from a file and displays them in the terminal.

    Args:
        file_name (str): The name of the file containing the contacts.
        page_size (int, optional): The number of contacts to display on each page. Defaults to 20.

    Returns:
        None: This function does not return any values.
    """
    with open(file_name, 'r') as file:
        print()
        print(file.readline(), end='')
        print(file.readline(), end='')
        while True:
            # Read 20 lines from the file
            lines = [file.readline() for _ in range(page_size)]

            # If no more lines are left, break the loop
            if not lines[0]:
                break

            for line in lines:
                if line:
                    print(line.strip())  # strip() removes any trailing newline characters

            if lines[-1]:
                print("\n\t\tPress Enter to continue or ('q' ->  Quit)")
            else:
                break
            # Wait for user input to continue or quit
            user_input = input()
            if user_input.lower() == 'q':
                break


# Function to add a new contact

def add_contact(file_name: str, new_contact: str, sequence_number_of_the_new_contact: int) -> str:
    """
    This function adds a new contact to a file.

    Args:
        file_name (str): The name of the file where the new contact will be added.
        new_contact (str): The information of the new contact, separated by commas.
        sequence_number_of_the_new_contact (int): The sequence number of the new contact.

    Returns:
        str: The information of the new contact, including the sequence number.
    """
    new_contact_fields = [contact_field.strip() for contact_field in new_contact.split(',')]
    with (open(file_name, 'a') as file):
        file.write(f"{sequence_number_of_the_new_contact} | " + " | ".join(new_contact_fields) + "\n")
    return f"{sequence_number_of_the_new_contact} | " + " | ".join(new_contact_fields) + "\n"


def edit_contact(file_name: str, line_number: int, edited_contact: str) -> None:
    """
    This function modifies the information of a contact in a file.

    Args:
        file_name (str): The name of the file containing the contacts.
        line_number (int): The line number of the contact to be modified. The first line has line number 1.
        edited_contact (str): The information of the modified contact, separated by commas.

    Returns:
        None: This function does not return any values.
    """
    edited_contact_fields = [contact_field.strip() for contact_field in edited_contact.split(',')]

    # Open the file in read mode
    with open(file_name, 'r') as file:
        lines = file.readlines()
        # Modify the content of the specified line
        lines[line_number + 2 - 1] = f"{line_number} | " + " | ".join(edited_contact_fields) + "\n"

    # Open the file in write mode to update its content
    with open(file_name, 'w') as file:
        file.writelines(lines)


# Function for deleting a contact

def delete_contact(file_name: str, line_number: int) -> str:
    """
    This function deletes a contact from a file.

    Args:
        file_name (str): The name of the file containing the contacts.
        line_number (int): The line number of the contact to be deleted. The first line has line number 1.

    Returns:
        str: The information of the deleted contact.

    """    # Open the file in read mode
    with open(file_name, 'r') as file:
        lines = file.readlines()

    # Open the file in write mode to update its content
    with open(file_name, 'w') as file:
        for index, line in enumerate(lines):
            # print(f"index = {index - 1}, line = {line}")
            if index - 1 < line_number:
                file.writelines(line)
            elif index - 1 == line_number:
                deleted_line = line
                continue
            else:
                line_fields = line.strip().split(' | ')[1:]
                contact_with_a_new_order_number = f"{index - 2} | " + " | ".join(line_fields) + "\n"
                file.write(contact_with_a_new_order_number)

    return deleted_line


# Function for searching contacts by characteristics
def search_contacts(file_name: str, key_word: str):
    """
    This function searches for contacts in a file based on a keyword.

    Args:
        file_name (str): The name of the file containing the contacts.
        key_word (str): The keyword to search for.

    Yields:
        Generator[str, None, None]: A generator that yields the information of the contacts that match the keyword.
    """
    with open(file_name, 'r') as file:
        file.readline()
        file.readline()
        contacts = file.readlines()

    for contact in contacts:
        if contact.lower().find(key_word) == -1:
            continue
        else:
            yield contact.strip()


def sharing(from_file: str, to_file: str) -> int:
    """
    This function shares the information of the contacts in one file to another file.

    Args:
        from_file (str): The name of the file containing the contacts to be shared.
        to_file (str): The name of the file where the shared contacts will be stored.

    Returns:
        int: The number of copied contacts.

    """
    information_to_be_shared = read_from(from_file)
    copied_contacts_number = append_to(to_file, information_to_be_shared)

    return copied_contacts_number


def create_file(new_file_name: str) -> str:
    """
    This function creates a new text file and writes the column headers to it.

    Args:
        new_file_name (str): The name of the new file.

    Returns:
        str: The name of the new file.

    """
    with open(f"{new_file_name}.txt", 'w') as f:
        f.write("N | First name | Last name | Patronymic | Organization | Work phone | Personal phone\n"
                "------------------------------------------------------------------------------------\n")

    return f"{new_file_name}.txt"
