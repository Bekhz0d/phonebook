# Determine the order number for a new contact
def determine_new_contact_id(file_name: str) -> int:
    """
    This function determines the next available contact ID by reading the contents of the specified file
    and incrementing the largest existing ID by 1.

    Args:
        file_name (str): The name of the file containing the contact data.

    Returns:
        int: The next available contact ID.

    Raises:
        FileNotFoundError: If the specified file does not exist.

    """
    new_contact_id = 0
    with open(file_name, 'r') as file:
        for _ in file:
            new_contact_id += 1
    return new_contact_id - 1


# Checking the validity of the contact entered by the user
def is_valid_contact_format(input_string: str) -> bool:
    """
    This function checks if the input string is in the correct format for a contact.

    Args:
        input_string (str): The input string to be checked.

    Returns:
        bool: True if the input string is in the correct format, False otherwise.

    """
    # Split the input string by comma and strip whitespace from each contact_field
    contact_fields = [contact_field.strip() for contact_field in input_string.split(',')]
    # Check if there are exactly six contact_fields
    if len(contact_fields) != 6:
        return False
    # Check if each contact field has non-zero length
    if not all(contact_fields):
        return False

    return True


# Function to get user input and validate it
def get_and_validate_input() -> str | None:
    """
    This function prompts the user to enter a new contact and validates the input.

    Returns:
        str: The user input, or 'q' to quit.

    """

    user_input = input("\nEnter a new contact in the format "
                       "'First Name, Last Name, Patronymic, Organization, Work Phone, Personal Phone'"
                       "\n('q' ->  Quit)"
                       "\n>>> ").strip()
    if user_input == 'q':
        return 'q'

    if is_valid_contact_format(user_input):
        return user_input
    else:
        print("\nInvalid format. Please enter the contact information in the specified format.")
        return None


def read_from(file_name: str):
    """
    This function reads from a file and yields the lines of the file.

    Args:
        file_name (str): The name of the file.

    Yields:
        str: A line from the file.

    """

    with open(file_name, 'r') as f:
        f.readline()
        f.readline()
        for line in f:
            yield line.strip()


def write_(file_name: str, new_contact_sequence_number: int, lines) -> int:
    """
    This function writes the file from the rest.

    Args:
        file_name (str): The name of the file.
        new_contact_sequence_number (int): The sequence number of the new contact to be written.
        lines (generator): A generator that yields the lines of the file.

    Returns:
        int: Number of rows copied.

    """
    copied_contacts_number = 0
    with open(file_name, 'a') as f:
        print()
        print()
        for line in lines:
            contact_fields = line.split(' | ')[1:]
            contact_data = " | ".join(contact_fields)
            f.write(f"{new_contact_sequence_number} | " + contact_data + "\n")
            print(f"COPIED  {contact_data}")
            copied_contacts_number += 1
            new_contact_sequence_number += 1
    return copied_contacts_number


def append_to(file_name: str, lines) -> int:
    """
    This function appends lines to a file.

    Args:
        file_name (str): The name of the file.
        lines (generator): A generator that yields the lines to be appended.

    Returns:
        int: Number of rows copied.

    """

    new_contact_sequence_number = determine_new_contact_id(file_name)

    if new_contact_sequence_number == 1:

        copied_contacts_number = write_(file_name, new_contact_sequence_number, lines)
        return copied_contacts_number

    # if the file does not have a table base
    elif new_contact_sequence_number < 1:  # 0 or -1
        with open(file_name, 'w') as f:
            f.write("N | First name | Last name | Patronymic | Organization | Work phone | Personal phone\n"
                    "------------------------------------------------------------------------------------\n")
        new_contact_sequence_number = 1
        copied_contacts_number = write_(file_name, new_contact_sequence_number, lines)
        return copied_contacts_number

    copied_contacts_number = write_(file_name, new_contact_sequence_number, lines)
    return copied_contacts_number
