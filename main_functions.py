from extra_functions import read_from, append_to


# Function for reading contacts from a file
def read_contacts(file_name, page_size=20):
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
def add_contact(file_name, new_contact, sequence_number_of_the_new_contact):
    new_contact_fields = [contact_field.strip() for contact_field in new_contact.split(',')]
    with (open(file_name, 'a') as file):
        file.write(f"{sequence_number_of_the_new_contact} | " + " | ".join(new_contact_fields) + "\n")
    return f"{sequence_number_of_the_new_contact} | " + " | ".join(new_contact_fields) + "\n"


def edit_contact(file_name, line_number, edited_contact):
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
def delete_contact(file_name, line_number):
    # Open the file in read mode
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
def search_contacts(file_name, key_word):
    with open(file_name, 'r') as file:
        file.readline()
        file.readline()
        contacts = file.readlines()

    for contact in contacts:
        if contact.lower().find(key_word) == -1:
            continue
        else:
            yield contact.strip()


def sharing(from_file, to_file):
    information_to_be_shared = read_from(from_file)
    transferred_contacts_number = append_to(to_file, information_to_be_shared)

    return transferred_contacts_number


def create_file(new_file_name):
    with open(f"{new_file_name}.txt", 'w') as f:
        f.write("N | First name | Last name | Patronymic | Organization | Work phone | Personal phone\n"
                "------------------------------------------------------------------------------------\n")

    return f"{new_file_name}.txt"
