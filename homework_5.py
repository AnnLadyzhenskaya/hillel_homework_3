"""
Запросить у пользователя число N - ширина треугольника.
"""
import sys

try:
    width = int(input("Enter the expected width: "))
except:
    sys.exit("Enter correct number")

"""
Вывести треугольник #1 с шириной N с помощью цикла for
*****
****
***
**
*
"""

print("\nFirst triangle")
for i in range(width, 0, -1):
    print("*" * i)

"""
Вывести треугольник #1 с шириной N с помощью цикла for
*
**
***
****
*****
"""

print("\nSecond triangle")
for i in range(1, width + 1):
    print("*" * i)

"""
Вывести треугольник #3 с шириной N с помощью цикла for
*****
 ****
  ***
   **
    *
"""

print("\nThird triangle")
space = 0
for i in range(width, 0, -1):
    print(" " * space + "*" * i)
    space += 1

"""
Вывести треугольник #4 с шириной N с помощью цикла for
    *
   **
  ***
 ****
*****
"""

print("\nFourth triangle")
space = width - 1
for i in range(1, width + 1):
    print(" " * space + "*" * i)
    space -= 1
