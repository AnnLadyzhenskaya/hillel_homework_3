"""
Задание #1:
Дано два множества A и B
В множестве А находятся имена должников за Сентябрь
В множестве B находятся имена должников за Октябрь
Найти:
* Вывести имена людей которые должны за Сентябрь и Октябрь
* Вывести должников за Октябрь у которых нет долга за Сентябрь
"""
import sys

A = {"Petrenko", "Schevchenko", "Tarasenko", "Nazarenko"}
B = {"Petrenko", "Schevchenko", "Tarasenko", "Honchar", "Kukhar"}

print(f"Должники за сентябрь и октябрь: {A.intersection(B)}")
print(f"Должники только за октябрь: {B.difference(A)}")

"""
Задание #2:
Права доступа
Вирус повредил систему прав доступа к файлам. Известно, что над каждым файлом можно производить
определенные действия:
запись – W;
чтение – R;
запуск – X.

На вход программе подается:
число n – количество файлов;
n строк с именами файлов и допустимыми операциями;
число m – количество запросов к файлам;
m запросов вида «операция файл».

Для каждого допустимого запроса программа должна возвращать OK, для недопустимого – Access denied.
"""

print("\nWORK WITH FILES:")

access_codes = {"R", "W", "X"}
dict_of_accesses = {"read": "R", "write": "W", "execute": "X"}
dict_of_files = {}
result_of_requested_access = []


# Проверка имени файла
def check_file_name(name):
    if name.find(".") == -1 or len(name) < 3 or name.rfind(".") == len(name) - 1 or name.find(".") == 0:
        sys.exit("Invalid file name")
    return True


def check_access_name(access):
    if access not in dict_of_accesses.keys():
        sys.exit("Invalid access name")


# Проверка на наличие расширения и уровня доступа
def validate_file_name(user_input):
    list_of_data = user_input.split()
    # Валидация количества слов
    if len(list_of_data) < 2:
        sys.exit("Invalid data")

    # Валидация имени файла
    file_name = list_of_data[0]
    check_file_name(file_name)

    # Валидация модификаторов доступа
    for code in list_of_data[1:]:
        if code not in access_codes:
            sys.exit("Invalid access code")


# Создание словаря с ключом в виде имени и значением в виде сета из доступов
def create_dict_access(user_input):
    file_name = user_input.split()[0]
    file_access = set(user_input.split()[1:])
    dict_of_files[file_name] = file_access


# Запрос данных о файлах и доступах от пользователя
def get_files_input():
    try:
        n = int(input("\nEnter the number of files: "))
    except:
        sys.exit("Enter correct number")
    for _ in range(0, n):
        file_with_access = input("\nEnter the name of file with access level: ")
        validate_file_name(file_with_access)
        create_dict_access(file_with_access)


get_files_input()


# Проверка на наличие одного вида доступа за раз, наличия файла и верного имени доступа
def check_data_input(requested_file):
    if len(requested_file.split()) > 2:
        sys.exit("Too many data")
    else:
        file_access = requested_file.split()[0]
        file_name = requested_file.split()[1]

        check_file_name(file_name)
        check_access_name(file_access)

        if file_name not in dict_of_files.keys():
            sys.exit("Wrong file name")
        if file_access not in dict_of_accesses.keys():
            sys.exit("Wrong access name")

        return {"name": file_name, "access": file_access}


# Проверка на наличие доступа к файлу
def check_access(file_with_access):
    file_name = file_with_access["name"]
    access_word = file_with_access["access"]
    access_code = dict_of_accesses[access_word]

    if access_code in dict_of_files[file_name]:
        result_of_requested_access.append("OK")
    else:
        result_of_requested_access.append("Access denied")


def print_results():
    print("\nResults:\n")
    for result in result_of_requested_access:
        print(result)


# Запрос доступов для файлов
def request_files_access():
    try:
        m = int(input("\nEnter the number of requests: "))
    except:
        sys.exit("Enter correct number")
    for _ in range(0, m):
        requested_file = input("\nEnter desired access level for file: ")
        file_with_access = check_data_input(requested_file)
        check_access(file_with_access)

    print_results()


request_files_access()

