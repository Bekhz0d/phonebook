from main_functions import read_contacts, add_contact, edit_contact, delete_contact, search_contacts, sharing, \
    create_file
from extra_functions import get_and_validate_input, determine_new_contact_id
import os

# # Create data for testing
# with open('RandomData 200.csv', 'r') as f:
#     data = f.readlines()
#
# with open('my_contacts.txt', 'w') as f:
#     f.write("N | First name | Last name | Patronymic | Organization | Work phone | Personal phone\n"
#             "------------------------------------------------------------------------------------\n")
#     for line in data:
#         clean_line = line.split(',')
#         clean_line_fields = [line.strip('"') for line in clean_line]
#         f.write(" | ".join(clean_line_fields))
#     f.write("\n")


# Main function
def main():
    """
    Main function that controls the program's flow.
    """
    file_name = 'my_contacts.txt'
    if not os.path.exists(file_name):
        """
        Creates a new file with the specified name if it does not exist.
        """
        create_file(file_name.split('.')[0])

    sequence_number_of_the_new_contact = determine_new_contact_id(file_name)

    if sequence_number_of_the_new_contact < 1:
        """
        Creates a new file with the specified name if it does not exist.
        """
        with open(file_name, 'w') as file:
            file.write("N | First name | Last name | Patronymic | Organization | Work phone | Personal phone\n"
                       "------------------------------------------------------------------------------------\n")
        sequence_number_of_the_new_contact = 1

    while True:
        print(f"\n\t--- File: {file_name} ---\n")
        print("  '1'  -> View contacts")
        print("  '2'  -> Add contact")
        print("  '3'  -> Edit contact")
        print("  '4'  -> Search contacts")
        print("  '55' -> Delete contact")
        print("  '6'  -> Import contacts")
        print("  '7'  -> Export contacts")
        print("  '8'  -> Clearing the file")
        print("  '9'  -> Switch to another file")
        print("  '0'  -> Create a new file")
        print("  'q'  ->  Quit")

        choice = input("\nChoose an action: ").strip()

        if choice == '1':
            """
            Reads the contents of the specified file and displays the contacts.
            """
            read_contacts(file_name)
            if sequence_number_of_the_new_contact == 1:
                print("\nThere are no contacts in the file.\n")
            print("------------------------------------------------------------------------------------")
            print(f"Number of contacts: {sequence_number_of_the_new_contact - 1}")

        elif choice == '2':
            """
            Prompts the user to enter a new contact and adds it to the file.
            """
            while True:
                new_contact = get_and_validate_input()
                if new_contact:
                    break

            if new_contact != 'q':
                added_contact = add_contact(file_name, new_contact, sequence_number_of_the_new_contact)
                sequence_number_of_the_new_contact += 1
                print(f"\n{added_contact} \nADDED SUCCESSFULLY")

        elif choice == '3':
            """
            Prompts the user to edit an existing contact and updates the file.
            """
            while True:
                contact_id = input("Enter the sequence number of the contact you want to edit ('q' ->  Quit)"
                                   ">>> ").strip()
                if contact_id == 'q':
                    break
                try:
                    contact_id = int(contact_id)
                except ValueError:
                    print("\nInvalid sequence number")
                    print("\nPlease, ", end='')
                if 0 < contact_id < sequence_number_of_the_new_contact:
                    while True:
                        edited_contact = get_and_validate_input()
                        if edited_contact:
                            break
                    edit_contact(file_name, contact_id, edited_contact)
                    print("\nThe contact EDITED SUCCESSFULLY")
                    break
                else:
                    print(f"\nThe contact in sequence number {contact_id} does not exist in the file."
                          " Sequence number is out of range. \nTry again...  ('q' ->  Quit)")

        elif choice == '4':
            """
            Prompts the user to enter a keyword and searches for matching contacts in the file.
            """
            key_word = input("\nEnter a keyword for the desired contact or contacts ('q' ->  Quit)"
                             ">>> ").strip().lower()
            if key_word != 'q':
                found_contacts = search_contacts(file_name, key_word)

                if found_contacts:
                    print("\n\nN | First name | Last name | Patronymic | Organization | Work phone | Personal phone\n"
                          "------------------------------------------------------------------------------------")

                    founded_contacts_number = 0
                    for contact in found_contacts:
                        print(contact)
                        founded_contacts_number += 1
                    print(f"------------------------------------------------------------------------------------"
                          f"\nNumber of founded contacts: {founded_contacts_number}\n")
                else:
                    print("\nContacts not found.")

        elif choice == '55':
            """
            Prompts the user to enter the sequence number of a contact and deletes it from the file.
            """
            while True:
                contact_id = input("Enter the sequence number of the contact you want to delete ('q' ->  Quit)"
                                   ">>> ").strip()
                if contact_id == 'q':
                    break

                try:
                    contact_id = int(contact_id)
                except ValueError:
                    print("\nInvalid sequence number")
                    print("\nPlease, ", end='')
                    continue

                if 0 < contact_id < sequence_number_of_the_new_contact:
                    deleted_contact = delete_contact(file_name, contact_id)
                    sequence_number_of_the_new_contact -= 1
                    print(f"""\n"{deleted_contact}" DELETED SUCCESSFULLY""")
                    break
                else:
                    print(f"\nThe contact in sequence number {contact_id} does not exist in the file."
                          " Sequence number is out of range. \nTry again... ('q' ->  Quit)")

        elif choice == '6':
            """
            Prompts the user to enter the path of a file to import and adds the contacts to the file.
            """
            while True:
                file_address = input("Enter the path to the file to be imported in the format"
                                     "'/path/to/your/file/your_file_name.txt' ('q' ->  Quit)"
                                     "\n>>> ").strip()
                if file_address == 'q':
                    break
                elif not file_address:
                    print("Please ", end="")
                    continue
                elif os.path.exists(file_address):
                    copied_contacts_number = sharing(from_file=file_address, to_file=file_name)
                    print(f"\n{copied_contacts_number} contacts have been COPIED SUCCESSFULLY")
                    sequence_number_of_the_new_contact += copied_contacts_number
                    break
                else:
                    print("\nThe file not found.")

        elif choice == '7':
            """
            Prompts the user to enter the path of a file to export and copies the contacts to the file.
            """
            while True:
                file_address = input("To export, enter the path of the file to be exported in the format"
                                     "'/path/to/your/file/your_file_name.txt' ('q' ->  Quit)"
                                     "\n>>> ").strip()
                if file_address == 'q':
                    break
                elif not file_address:
                    print("Please, ", end="")
                    continue
                elif os.path.exists(file_address):
                    copied_contacts_number = sharing(from_file=file_name, to_file=file_address)
                    print(f"\n{copied_contacts_number} contacts have been COPIED SUCCESSFULLY")
                    break
                else:
                    print("\nThe file not found.")

        elif choice == '8':
            """
            Prompts the user to confirm clearing the file and deletes all the contents.
            """
            while True:
                confirm = input("\nAre you sure you want to clear the file?"
                                "\n  'yes' -> Yes\n  'no'  -> No\n  'q'   ->  Quit"
                                "\n>>> ").strip()
                if confirm == 'q' or confirm == 'no':
                    break
                elif confirm == 'yes':
                    create_file(file_name.split('.')[0])
                    print("\nFile CLEARED SUCCESSFULLY\n")
                    sequence_number_of_the_new_contact = determine_new_contact_id(file_name)
                    break

        elif choice == '9':
            """
            Lists the available files and prompts the user to select a new file.
            """
            files = os.listdir()
            txt_files = []
            for file in files:
                if file.endswith('.txt'):
                    txt_files.append(file)

            while True:
                print()
                for i, name in (enumerate(txt_files)):
                    print(f"'{i + 1}' ->  {name}")

                select = input("\nChoose an action ('q' ->  Quit): ").strip()
                if select == 'q':
                    break

                try:
                    select = int(select)
                except ValueError:
                    print("\nInvalid choice, Try again... \n")
                    continue

                if 0 < select < len(txt_files) + 1:
                    file_name = txt_files[select - 1]
                    sequence_number_of_the_new_contact = determine_new_contact_id(file_name)
                    break
                else:
                    print("\nInvalid choice, Try again... \n")

        elif choice == '0':
            """ Create new file """
            while True:
                new_file_name = input("Enter the name of the new file ('q' ->  Quit)"
                                      ">>> ").strip()
                if new_file_name == 'q':
                    break
                elif not new_file_name:
                    print("Please, ", end="")
                    continue
                elif os.path.exists(f"{new_file_name}.txt"):
                    print(f"{new_file_name}.txt already exists.")
                    continue
                file_name = create_file(new_file_name)
                print(f"\n{new_file_name}.txt CREATED SUCCESSFULLY\n")
                sequence_number_of_the_new_contact = 1
                break

        elif choice == 'q':
            """ Quit """
            print("\nTHANK TOU FOR USING!\n")
            break

        else:
            print("\nInvalid selection input. Try again...\n")


if __name__ == "__main__":
    main()
