"""
Написать декоратор call_times, который будет принимать в качестве параметра file_name,
считать количество вызовов функций и записывать в файл в формате
f'{func_name} была вызвана {count} раза.\n'
"""


def call_times(filename):
    counts_dict = {}

    def wrapper(func):
        def inner(*args, **kwargs):
            if func not in counts_dict.keys():
                counts_dict[func] = 1
                with open(filename, "a") as f:
                    f.write(f"{func.__name__} была вызвана {counts_dict[func]} раза.\n")
            else:
                counts_dict[func] += 1
                with open(filename, "r") as f:
                    data = f.readlines()
                with open(filename, "w") as f:
                    for line in data:
                        if f"{func.__name__}" not in line:
                            f.write(line)
                        else:
                            f.write(f"{func.__name__} была вызвана {counts_dict[func]} раза.\n")
        return inner
    return wrapper


@call_times("res/txt/foo.txt")
def foo():
    pass


@call_times("res/txt/foo.txt")
def boo():
    pass


@call_times("res/txt/calls.txt")
def doo():
    pass


foo()
boo()
foo()
foo()
boo()
doo()
