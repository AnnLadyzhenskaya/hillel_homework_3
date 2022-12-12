"""
Написать функцию которая принимает целое число - number.
Функция должна возвращать 'yes' если number является степенью двойки,
иначе 'no'. Запрещено пользоваться функцией или оператором возведение в степень.

Пример:
is_power_of_two(256) # 'yes' потому что 2 в 8 степени это 256
is_power_of_two(125) # 'no' потому что это не степень двойки
"""


def is_power_of_two(number):
    if not isinstance(number, int) or number <= 0:
        return "Wrong number"

    if number == 1:
        return "yes"

    if number % 2 == 0:
        number = number//2
        return is_power_of_two(number)
    else:
        return "no"


print(f"256 is power of two: {is_power_of_two(256)}")
print(f"125 is power of two: {is_power_of_two(125)}")
print(f"8 is power of two: {is_power_of_two(8)}")
print(f"1 is power of two: {is_power_of_two(1)}")
print(f"0 is power of two: {is_power_of_two(0)}")
print(f"55 is power of two: {is_power_of_two(55)}")
print(f"-7 is power of two: {is_power_of_two(-7)}")
print(f"56.6 is power of two: {is_power_of_two(56.6)}")
