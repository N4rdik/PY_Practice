from data_create import name_data, surname_data, phone_data, address_data

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные\n\n"
    f"1 Вариант: \n"
    f"{name}\n{surname}\n{phone}\n{address}\n\n"
    f"2 Вариант: \n"
    f"{name}; {surname}; {phone}; {address}\n"
    f"Выберите вариант: \n"))
    while var !=1 and var !=2:
            print("Неправильный ввод")
            var = int(input("Введите 1 или 2: \n"))
    if var == 1:
        with open ("data_first_variant.csv", "a", encoding="utf-8") as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    elif var == 2:
        with open ("data_second_variant.csv", "a", encoding="utf-8") as f:
           f.write(f"\n {name}; {surname}; {phone}; {address}\n")

def print_data():
    print("Данные из первого справочника: \n")
    with open ("data_first_variant.csv", "r", encoding="utf-8") as f:
        data_first = f.readlines()
        data_first_list = []
        j=0
        for i in range(len(data_first)):
            if data_first[i] == '\n' or i == len(data_first)-1:
                data_first_list.append(''.join(data_first[j:i+1]))
                j=i
        print(''.join(data_first_list))


    print("Данные из второго справочника: \n")
    with open ("data_second_variant.csv", "r", encoding="utf-8") as f:
        data_second = f.readlines()
        print(*data_second)


def remove_empty_lines(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines()

    modified_lines = []
    for line in lines:
        if line.strip():  # проверяем, что строка не пустая
            modified_lines.append(line)

    with open(file_name, "w") as file:
        for line in modified_lines:
            file.write(line)

def edit_data():
    #remove_empty_lines("data_first_var.csv")
    #remove_empty_lines("data_second_var.csv")
    choice = int(input("Выберите вариант:\n1 - Изменить данные в первом файле\n2 - Изменить данные во втором файле\n"))
    while choice != 1 and choice != 2:
        print("Неправильный ввод")
        choice = int(input("Выберите вариант:\n1 - Изменить данные в первом файле\n2 - Изменить данные во втором файле\n"))

    if choice == 1:
        with open("data_first_var.csv", 'r', encoding='utf-8') as f:
            data = f.readlines()        

        print("Доступные данные для изменения:")
        print(*data)

        line_number = int(input("Введите номер строки, которую хотите изменить: "))
        while line_number < 1 or line_number > len(data):
            print("Неправильный номер строки")
            line_number = int(input("Введите номер строки, которую хотите изменить: "))

        new_data = input("Введите новые данные: ") 

        data[line_number-1] = new_data + " \n"

        with open("data_first_var.csv", 'w', encoding='utf-8') as f:
            f.writelines(data)
        print ("Спасибо, изменения сохранены")

    elif choice == 2:
        with open("data_second_var.csv", 'r', encoding='utf-8') as f:
            data = f.readlines()            

        print("Доступные данные для изменения:")
        print(*data)

        line_number = int(input("Введите номер строки, которую хотите изменить: "))
        while line_number < 1 or line_number > len(data):
            print("Неправильный номер строки")
            line_number = int(input("Введите номер строки, которую хотите изменить: "))

        new_data = name_data() + "; " + surname_data() + "; " + phone_data() + "; " + address_data()

        data[line_number-1] = new_data + "\n"

        with open("data_second_var.csv", 'w', encoding='utf-8') as f:
            f.writelines(data)
        print ("Спасибо, изменения сохранены")


def delete_data():
    choice = int(input("Выберите вариант:\n1 - Удалить данные из первого файла\n2 - Удалить данные из второго файла\n"))
    while choice != 1 and choice != 2:
        print("Неправильный ввод")
        choice = int(input("Выберите вариант:\n1 - Удалить данные из первого файла\n2 - Удалить данные из второго файла\n"))

    if choice == 1:
        with open("data_first_var.csv", 'r', encoding='utf-8') as f:
            data = f.readlines()

        print("Доступные данные для удаления:")
        print(*data)

        line_number = int(input("Введите номер строки, которую хотите удалить: "))
        while line_number < 1 or line_number > len(data):
            print("Неправильный номер строки")
            line_number = int(input("Введите номер строки, которую хотите удалить: "))

        del data[line_number-1]

        with open("data_first_var.csv", 'w', encoding='utf-8') as f:
            f.writelines(data)
        print ("Спасибо, данные удалены")

    elif choice == 2:
        with open("data_second_var.csv", 'r', encoding='utf-8') as f:
            data = f.readlines()

        print("Доступные данные для удаления:")
        print(*data)

        line_number = int(input("Введите номер строки, которую хотите удалить: "))
        while line_number < 1 or line_number > len(data):
            print("Неправильный номер строки")
            line_number = int(input("Введите номер строки, которую хотите удалить: "))

        del data[line_number-1]

        with open("data_second_var.csv", 'w', encoding='utf-8') as f:
            f.writelines(data)
        print ("Спасибо, данные удалены")

