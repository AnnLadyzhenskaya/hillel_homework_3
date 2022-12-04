"""
Задание 1
Дан файл с произвольным текстом,
необходимо найти все числа в файле и записать в список numbers
"""
import sys

#
# def find_number(text):
#     # Убираем знаки препинания для кейсов 222? или 1! в тексте
#     text_without_symbols = "".join(char for char in text if (char.isalnum() or char == " "))
#
#     list_from_text = text_without_symbols.split()
#     for word in list_from_text:
#         if word.isdigit():
#             return int(word)
#
#
# with open("res/txt/task_9.1.txt", "r") as f:
#     numbers = [num for num in map(find_number, f) if num is not None]
#
# print(f"List of numbers: {numbers}")


"""
Задание 2
Запросить у пользователя текст и записать его в файл data.txt
"""

# with open("res/txt/data.txt", "w") as f:
#     f.write(input("\nEnter the text you want to save: "))


"""
Задание 3
Запросить у пользователя число N и запросить N чисел у пользователя, 
потом записать их в файл numbers.txt через пробел
"""

# try:
#     N = int(input("Enter a number of numbers: "))
# except:
#     sys.exit("Wrong data")
#
#
# def extract_number(data):
#     if data.isdigit():
#         return data
#     elif data.find(".") != -1:
#         try:
#             float(data)
#             return data
#         except:
#             sys.exit("Enter correct number")
#     else:
#         sys.exit("Enter correct number")
#
#
# numbers = []
# for _ in range(0, N):
#     numbers.append(extract_number(input("Enter number: ")))
#
# with open("res/txt/numbers.txt", "w") as f:
#     f.write(" ".join(numbers))


"""
Задание 4
Сгенерировать 100 рандомных чисел и записать их в файл random_numbers.txt, 
где одна строка = одно число
"""

