"""
Задание 1:
Запросить у пользователя 5 чисел и записать их в список
"""

list_of_numbers = []
for i in range(0, 5):
    number = int(input(f"Enter a number #{i + 1}: "))
    list_of_numbers.append(number)

print(list_of_numbers)


"""
Задание 2:
Дан список A = [1, 2, 3, 4, 5]
Удалить последнее число из списка
"""

A = [1, 2, 3, 4, 5]
A.pop()
print(f"\nEdited list: {A}")


"""
Задание 3:
Запросить у пользователя 10 чисел и записать их в список A
Запросить у пользователя число N
Вывести пользователю сколько в списке A повторяется число N
"""

A = []
for i in range(0, 10):
    number = int(input(f"Enter a number #{i + 1}: "))
    A.append(number)

searchable_number = int(input("\nEnter a number you want to find: "))
count_in_list = A.count(searchable_number)
print(f"Your number was found {count_in_list} times")


"""
Задание 4:

Запросить у пользователя число N
Запросить у пользователя N чисел и записать их в список A
Вывести список в обратной последовательности
"""

N = int(input("\nHow many numbers do you need?: "))
A = []
for i in range(0, N):
    number = int(input(f"Enter a number #{i + 1}: "))
    A.append(number)

print(f"Reversed list: \n {A[::-1]}")


"""
Задание 5:
Запросить у пользователя 5 чисел и записать их в список A
Записать все числа из списка A которые больше 5 в список C
"""

A = []
for i in range(0, 5):
    number = int(input(f"Enter a number #{i + 1}: "))
    A.append(number)

C = [number for number in A if number > 5]
print(f"Numbers higher then 5: {C}")


"""
Задание 6:
Запросить у пользователя число N
Запросить у пользователя N целых чисел и записать их в список A
Найти в нем минимальное и максимальное число с помощью цикла 
(запрещено использовать функцию min и max). Вывести эти числа.
"""

N = int(input("\nHow many numbers do you need?: "))
A = []
for i in range(0, N):
    number = int(input(f"Enter a number #{i + 1}: "))
    A.append(number)

max_num = A[0]
min_num = A[0]

for num in A:
    max_num = num if num > max_num else max_num
    min_num = num if num < min_num else min_num

print(f"Max number is {max_num}, min number is {min_num}")


"""
Задание 7:
Пользователь вводит текст нужно вывести количество чисел в этом тексте
Пример:
> 'Lorem 222 ipsum, 123 dolor 1 sit amet
Количество чисел: 3
"""

text_input = input("\nEnter text: ")

# Убираем знаки препинания для кейсов 222? или 1! в тексте
text_without_symbols = "".join(char for char in text_input if (char.isalnum() or char == " "))
list_from_text = text_without_symbols.split()

count_of_numbers = 0
for i in list_from_text:
    if i.isdigit():
        count_of_numbers += 1

print(f"\nКоличество чисел: {count_of_numbers}")




