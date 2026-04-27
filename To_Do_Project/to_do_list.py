print("#" * 30,"\nВас приветствует to do list")
main_list = []
print("Выберите действие:\n1 - Добавить задачу\n2 - Показать список\n3 - Отметить выполнение\n4 - Удалить задачу\n5 - Выйти")
while True:
    user_input = input("Введите число: ")
    match user_input:
        case "1":
            new_task = input("Введите задачу: ")
            main_list.append(new_task)
            print("Задача успешно добавлена!")
        case "2":
            if not main_list:
                print("У вас отсутствуют задачи")
            for index, task in enumerate(main_list, start=1):
                print(f"{index}) {task}")
        case "3":
            number_task = int(input("Введите номер задачи, которая выполненна: "))
            real_index = number_task - 1
            if main_list[real_index].endswith(" - СДЕЛАНО"):
                print("Задача уже завершена")
            else:
                main_list[real_index] += " - СДЕЛАНО"
        case "4":
            if not main_list:
                print("Вы еще не написали ни одной задачи.")
                continue
            else:
                number_task = int(input("Номер удаляемой задачи: "))
                real_index = number_task - 1
                del main_list[real_index]
                print(f"Задача {number_task} успешно удаленна")
        case "5":
            break
        case _:
            print("Извините данной команды не существует")
            
