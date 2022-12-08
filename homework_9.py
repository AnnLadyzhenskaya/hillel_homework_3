"""
Задание 1
Дан файл с произвольным текстом,
необходимо найти все числа в файле и записать в список numbers
"""
import random
import sys
import functools
import itertools


def find_number(text):
    # Убираем знаки препинания для кейсов 222? или 1! в тексте
    text_without_symbols = "".join(char for char in text if (char.isalnum() or char == " "))

    list_from_text = text_without_symbols.split()
    for word in list_from_text:
        if word.isdigit():
            return int(word)


with open("res/txt/random_text.txt", "r") as f:
    numbers = [num for num in map(find_number, f) if num is not None]

print(f"List of numbers: {numbers}")


"""
Задание 2
Запросить у пользователя текст и записать его в файл data.txt
"""

with open("res/txt/data.txt", "w") as f:
    f.write(input("\nEnter the text you want to save: "))


"""
Задание 3
Запросить у пользователя число N и запросить N чисел у пользователя, 
потом записать их в файл numbers.txt через пробел
"""

try:
    N = int(input("Enter a number of numbers: "))
except:
    sys.exit("Wrong data")


def extract_number(data):
    if data.isdigit():
        return data
    elif data.find(".") != -1:
        try:
            float(data)
            return data
        except:
            sys.exit("Enter correct number")
    else:
        sys.exit("Enter correct number")


numbers = []
for _ in range(0, N):
    numbers.append(extract_number(input("Enter number: ")))

with open("res/txt/numbers.txt", "w") as f:
    f.write(" ".join(numbers))


"""
Задание 4
Сгенерировать 100 рандомных чисел и записать их в файл random_numbers.txt, 
где одна строка = одно число
"""

random_numbers = [random.randint(1, 1000) for _ in range(100)]

random_numbers_for_write = list(map(lambda x: str(x) + "\n", random_numbers))
with open("res/txt/random_numbers.txt", "w") as f:
    f.writelines(random_numbers_for_write)


"""
Задание 5
Дан файл с произвольным текстом, 
нужно найти количество слов в файле и вывести пользователю

ЧИСЛА ТАКЖЕ СЧИТАЮ ОТДЕЛЬНЫМ СЛОВОМ, так как в ТЗ не указано обратное
"""

with open("res/txt/random_text.txt", "r") as f:
    count = 0
    for line in f:
        list_line = line.split()
        count += len(list_line)

print(f"Количество слов: {count}")


"""
Задание 6
Дан файл в котором записаны числа через пробел, 
необходимо вывести пользователю сумму этих чисел

Предполагаем, что в файле действительно только числа
"""

with open("res/txt/numbers_for_sum.txt", "r") as f:
    sum_of_nums = 0
    nums = f.readline()
    sum_of_nums = functools.reduce(lambda a, b: int(a) + int(b), nums.split())

print(f"Сумма чисел из файла numbers_for_sum.txt: {sum_of_nums}")


"""
Задание 7
Дан файл в котором записан текст, необходимо вывести топ 5 строк 
которые чаще всего повторяются, пример:
'в' - 20 раз
'привет' - 10 раз
'как' - 9 раз
'у' - 7
'world' - 4

Не через Collections, раз уже о нем не говорили на занятии
"""


# Создаем словарь из строки с количеством вхождений каждого слова
def create_dict_with_words_count(string):
    list_of_words = string.split()
    dict_with_words_count = {}
    for word in list_of_words:
        if word in dict_with_words_count.keys():
            dict_with_words_count[word] += 1
        else:
            dict_with_words_count[word] = 1

    return dict_with_words_count


# Сопоставляем два словаря с количеством вхождений слов
def compose_dicts(new_dict, old_dict):
    for key in new_dict.keys():
        if key not in old_dict.keys():
            old_dict[key] = new_dict[key]
        else:
            old_dict[key] = new_dict[key] + old_dict[key]

    return old_dict


with open("res/txt/random_text.txt", "r") as f:
    result_dict = {}
    for line in f:
        words_with_count = create_dict_with_words_count(line)
        result_dict = compose_dicts(words_with_count, result_dict)

    sorted_result = dict(sorted(result_dict.items(), key=lambda item: item[1], reverse=True))
    sorted_top_5 = dict(itertools.islice(sorted_result.items(), 0, 5))

    print("\nТоп-5 слов в тексте:\n")
    for key in sorted_top_5.keys():
        print(f"{key} : {sorted_top_5[key]} раз")


