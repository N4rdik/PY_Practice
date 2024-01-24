def count_contact(contact):
    return len(contact)


def create_new_contact(contacts):
    information = []
    current_id = count_contact(contacts)
    information.append(input("Enter contact name: "))
    information.append(input("Enter contact phone number: "))
    information.append(input("Enter contact group: "))
    contacts[current_id] = information


def show_contacts(names):
    for key in names:
        print(f"id контакта: {key}, данные контакта: {names[key]}")



def change_contact_information(contacts_dict):
    id_to_change = input("Enter id of contact to change contact info: ")
    if contacts_dict.get(id_to_change):
        information = []
        information.append(input("Enter contact name: "))
        information.append(input("Enter contact phone number: "))
        information.append(input("Enter contact group: "))
        contacts_dict[id_to_change] = information
    else:
        print("Id not found!")


def convert_file_to_dict(file_name):
    result = {}
    with open(file_name) as file:
        lines = file.readlines()
        for line in lines:
            part1 = line.strip().split(";")
            result[part1[0]] = part1[1:]
    return result


def find_contact(contact_list):
    find_data = input('Введите данные для поиск:\n')
    count = 0
    for key, value in contact_list.items():
        if find_data.lower() in str(value).lower():
            print(f'id {key}:', end='\t')
            print(*list(value), sep=', ', end='')
            count += 1
    if count == 0:
        print('Контакт не найден!')
    print()


def delete_contact(names):
    show_contacts(names)
    id = input("Enter id which you wanna delete: ")
    if names.get(id):
        del names[id]
        print("Contact deleted successfully")
        show_contacts(names)
    else:
        print("Id not found.")


def save_changes(file_name, contact):
    with open(file_name, 'w') as file:
        for key, value in contact.items():
            file.write(f"{key};{value[0]};{value[1]};{value[2]}\n")


def copy_line_in_another_file(form_copy_file, in_copy_file):
    with open(form_copy_file, 'r') as file:
        lines = file.readlines()
        for line in range(0, len(lines)):
            print(f'Number to copy[{line}]  {lines[line]}', end='')
        with open(in_copy_file, 'a') as file:
            number_line = int(input("Enter number what you need to copy: "))
            if number_line >= 0 and number_line < len(lines):
                file.write(lines[number_line] + '\n')
