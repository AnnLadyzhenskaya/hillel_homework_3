"""
Задание 1:
Пользователь вводит слово, если это слово является полиндромом, то вывести '+', иначе '-'
"""

word = input("Enter your word: ")
result = "unknown"
result = "+ " if word == word[::-1] else "-"

print(f"Your word is palindrom: {result}")


"""
Задание 2:
Пользователь вводит текст и слово которое нужно найти, 
если это слово есть в тексте, вывести 'YES', иначе 'NO'
"""

text = input("\nEnter text: ")
word_for_search = input("Enter the word you want to find: ")

is_word_present = "YES" if text.find(word_for_search) > -1 else "NO"
print(f"This word is in the text: {is_word_present}")


"""
Задание 3:
Пользователь вводит строку. Если она начинается на 'abc', то заменить их на 'www', 
иначе добавить в конец строки 'zzz'.
"""

string = input("\nEnter any string: ")
new_string = string.replace("abc", "www") if string.startswith("abc") else string + "zzz"
print(f"New string is {new_string}")

"""
Задание 4:
Пользователь вводит текст, удалить в тексте все цифры и вывести строку пользователю.
"""
text = input("\nEnter any text: ")
text_without_digits = "".join(char for char in text if not char.isdigit())

print(f"Text without digits is:\n{text_without_digits}")


"""
Задание 5:
Написать валидатор для почты. Пользователь вводит почту, а программа должна проверить,
что в почте есть символ '@' и '.', и если это так, то вывести "YES", иначе "NO"

Комментарий:
mail.find("@") > 0, так как символ @ не может быть первым,
также символ "." должен быть после @
последним символов должна быть буква
"""

mail = input("Enter email: ")
result = "YES" if 0 < mail.find("@") < mail.rfind(".") and mail.count("@") == 1 and mail[-1].isalpha() else "NO"
print(f"Email is correct: {result}")



