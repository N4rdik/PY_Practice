
import file_opener_reader as frw
def print_menu():
        print("1. Create contact")
        print("2. Change contact")
        print("3. Find contact")
        print("4. Delete contact")
        print("5. Show contacts")
        print("6. Copy line in another file")
        print("7. Save changes")
        # count_id = 0
def main():
    phone_first = "phones.txt"
    second_file = "another_file.txt"
    contacts = frw.convert_file_to_dict(phone_first)
    while True:
        print_menu()
        input_number = input()
        if input_number == "1":
            frw.create_new_contact(contacts)
        elif input_number == "2":
            frw.change_contact_information(contacts)
        elif input_number == "3":
            frw.find_contact(contacts)
        elif input_number == "4":
            frw.delete_contact(contacts)
        elif input_number == "5":
            frw.show_contacts(contacts)
        elif input_number == "6":
             frw.copy_line_in_another_file(phone_first, second_file)
        elif input_number == "7":
            frw.save_changes(phone_first, contacts)
        else:
            print("Такого пункта меню не существует! попробуйте снова!")

if __name__ == "__main__":
    main()