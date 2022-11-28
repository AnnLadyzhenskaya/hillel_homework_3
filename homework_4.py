"""
Пользователь вводит с клавиатуры три числа в переменные a, b, c.
Если все числа больше 10 и первые два числа делятся на 3, то вывести yes, иначе no
"""

a = int(input("Enter number: "))
b = int(input("Enter number: "))
c = int(input("Enter number: "))

result = "unknown"
if (a > 10 and b > 10 and c > 10) and (a % 3 == 0 and b % 3 == 0):
    result = "yes"
else:
    result = "no"
print(f"All numbers are higher then 10 and first two are divided by 3: {result}")

"""
Пользователь вводит с клавиатуры три числа в переменные a, b, c. 
Найдите наибольшее число из них и запишите в переменную max.
"""

numbers = [a, b, c]
max_number = numbers[0]
for number in numbers:
    if number > max_number:
        max_number = number

print(f"Max number is: {max_number}")


"""
Пользователь с клавиатуры вводит трех значное число в переменную number.
Переставьте первую и последнюю цифру переменной number, 
полученный результат запишите в переменную reversed_number
"""

number = int(input("Enter three-digit number: "))
first_num = number // 100
second_num = number // 10 % 10
third_num = number % 10
reversed_number = third_num*100 + second_num*10 + first_num

print(f"Reversed number is: {reversed_number}")
