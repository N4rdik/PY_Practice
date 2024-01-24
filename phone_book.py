from logger import input_data, print_data, edit_data, delete_data

def print_menu():
        print(f"Здраствуйте, программа телефонна книжка. Функции программы: \n"
              f"1 - Запись данных \n"
              f"2 - Вывод данных \n"
              f"3 - Изменение данных в справочнике \n"
              f"4 - Удаление данных из справочника \n")
        command = int(input(f"Введите номер функции:\n"))
        if command <= 0 or command >4:
            print("Неправильный ввод")
            command = int(input(f"Такой функции нет! \n"
                                f"Функции программы: \n"
                                f"1 - Запись данных \n"
                                f"2 - Вывод данных \n"
                                f"3 - Изменение данных в справочнике \n"
                                f"4 - Удаление данных из справочника \n"
                                f"Введите номер функции:\n"))
        elif command == 1:
            input_data()
        elif command == 2:
            print_data()
        elif command == 3:
            edit_data()
        elif command == 4:
            delete_data()
    

print_menu()
