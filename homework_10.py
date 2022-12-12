"""
Напишите функцию change(lst), которая принимает список
и меняет местами его первый и последний элемент.
В исходном списке минимум 2 элемента.
"""
import os.path


def change(lst):
    if not isinstance(lst, list):
        print("Wrong data type")
        return
    if len(lst) < 2:
        print("List is too short")
        return

    last_index = len(lst) - 1
    original_first_el = lst[0]
    lst[0] = lst[last_index]
    lst[last_index] = original_first_el

    print(f"New list is: {lst}")
    return lst


# change([567, "String", (1, "Test", 4.5)])
# change([567])
# change(567)

"""
Напишите функцию to_dict(lst), которая принимает аргумент в виде списка 
и возвращает словарь, в котором каждый элемент списка является и ключом и значением. 
Предполагается, что элементы списка будут соответствовать правилам задания ключей в словарях.
"""


# Удаляем кортеж, если в нем есть мутабельные элементы или другие кортежи,
# так как я ленивый программист и ленюсь писать рекурсию
# на проверку элементов в кортежах внутри кортежей

def filter_tuple_with_mutables(obj):
    if isinstance(obj, tuple):
        for el in obj:
            if isinstance(el, (list, dict, set, tuple)):
                return False
    return True


def to_dict(lst):
    if not isinstance(lst, list):
        print("Wrong data type")
        return

    list_of_immutables = list(filter(lambda x: not isinstance(x, (list, dict, set)), lst))
    list_of_immutables_in_nested_elements = list(filter(filter_tuple_with_mutables, list_of_immutables))

    dict_from_list = {el: el for el in list_of_immutables_in_nested_elements}
    print(dict_from_list)

    return dict_from_list


# to_dict(["String", {34, False}, "Str2", 45, {"Str": 45, "Str2": "Str3"},
#          45.5, True, [1, 45, "Str"], ("Str", []), (1, 2)])


"""
Напишите функцию sum_range(start, end), 
которая суммирует все целые числа от значения «start» до величины «end» включительно. 
Если пользователь задаст первое число большее чем второе, просто поменяйте их местами.

Отрицательные инты не отбрасываю, так как ТЗ не предусмотрено
"""


def sum_range(start, end):

    if not (isinstance(start, int) and isinstance(end, int)):
        print("Wrong values")
        return

    if start > end:
        original_start = start
        start = end
        end = original_start

    result_sum = sum(range(start, end + 1))
    print(result_sum)

    return result_sum


# sum_range(15, 10)


"""
Напишите функцию read_last(lines, file), которая будет открывать определенный файл file 
и выводить на печать построчно последние строки в количестве lines 
(на всякий случай проверим, что задано положительное целое число).
"""


def read_lines(lines, file):
    if not isinstance(lines, int) or lines <= 0:
        print("Wrong lines number")
        return

    if not isinstance(file, str):
        print("Wrong file name")
        return

    if os.path.exists(file):
        with open(file, "r") as f:
            print(*f.readlines()[-lines:], sep="")
    else:
        print("File does not exist")


# read_lines(3, "/text.tx")
# read_lines(3, "res/txt/random_text.txt")


