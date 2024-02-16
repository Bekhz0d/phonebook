# Determine the order number for a new contact
def determine_new_contact_id(file_name: str) -> int:
    """
    Determines the order number for the new contact to be written to the file.
    Counts lines in file, subtracts 2 (file base is 2 lines), adds 1 because indexing starts at 0

    Parameters:
        file_name: The name of the file

    Returns:
        int: The order number of the new contact
    """
    new_contact_id = 0
    with open(file_name, 'r') as file:
        for _ in file:
            new_contact_id += 1
    """ The reason for subtract of 2 is that the first 2 lines of our file form the basis of the table and 
    since indexing starts at 0, we add 1 -> '- 2 + 1 = - 1' """
    return new_contact_id - 1


# Checking the validity of the contact entered by the user
def is_valid_contact_format(input_string):
    """
    Checks if information is entered for each field of the contact in the format
    "First Name, Last Name, Patronymic, Organization, Work Phone, Personal Phone"

    Parameters:
        input_string (string): user input

    Returns:
        boolean: whether the data entered by the user is correct or in an incorrect format
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
def get_and_validate_input():
    """
    Function to get user input and validate it

    Returns:
        string: user input
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


def read_from(file_name):
    """
    Function to read from a file

    Parameters:
        file_name (string): The name of the file

    Returns:
        generator: A generator that yields the lines of the file
    """

    with open(file_name, 'r') as f:
        f.readline()
        f.readline()
        for line in f:
            yield line.strip()


def append_to(file_name, lines):
    """
    Function to write the file from the rest

    Parameters:
        file_name (string): The name of the file
        lines (generator): A generator that yields the lines of the file

    Returns:

    """

    new_contact_sequence_number = determine_new_contact_id(file_name)

    if new_contact_sequence_number == 1:

        transferred_contacts_number = 0
        with open(file_name, 'a') as f:
            print()
            print()
            for line in lines:
                contact_fields = line.split(' | ')[1:]
                contact_data = " | ".join(contact_fields)
                f.write(f"{new_contact_sequence_number} | " + contact_data + "\n")
                print(f"TRANSFERRED  {contact_data}")
                transferred_contacts_number += 1
                new_contact_sequence_number += 1
        return transferred_contacts_number

    elif new_contact_sequence_number < 1:  # 0 or -1
        with open(file_name, 'w') as f:
            f.write("N | First name | Last name | Patronymic | Organization | Work phone | Personal phone\n"
                    "------------------------------------------------------------------------------------\n")
        new_contact_sequence_number = 1

        transferred_contacts_number = 0
        with open(file_name, 'a') as f:
            print()
            print()
            for line in lines:
                contact_fields = line.split(' | ')[1:]
                contact_data = " | ".join(contact_fields)
                f.write(f"{new_contact_sequence_number} | " + contact_data + "\n")
                print(f"TRANSFERRED  {contact_data}")
                transferred_contacts_number += 1
                new_contact_sequence_number += 1
        return transferred_contacts_number

    transferred_contacts_number = 0
    with open(file_name, 'a') as f:
        print()
        print()
        for line in lines:
            contact_fields = line.split(' | ')[1:]
            contact_data = " | ".join(contact_fields)
            f.write(f"{new_contact_sequence_number} | " + contact_data + "\n")
            print(f"TRANSFERRED  {contact_data}")
            transferred_contacts_number += 1
            new_contact_sequence_number += 1
    return transferred_contacts_number
