"""
Написать декоратор call_times, который будет принимать в качестве параметра file_name,
считать количество вызовов функций и записывать в файл в формате
f'{func_name} была вызвана {count} раза.\n'
"""
import fileinput
import os.path
import time


def call_times(filename):
    counts_dict = {}

    def wrapper(func):
        def inner(*args, **kwargs):
            if func not in counts_dict.keys():
                counts_dict[func] = 1
                with open(filename, "a") as f:
                    f.write(f"{func.__name__} была вызвана {counts_dict[func]} раза.\n")
            else:

                with fileinput.FileInput(filename, inplace=True) as f:
                    for line in f:
                        if f"{func.__name__}" in line:
                            print(line.replace(f"{counts_dict[func]} раза", f"{counts_dict[func] + 1} раза"), end="")
                            counts_dict[func] += 1
                        else:
                            print(line, end="")
        return inner
    return wrapper


def call_times_v2(filename):
    call_times_v2.counts_dict = {}

    def wrapper(func):
        def inner(*args, **kwargs):
            inner.calls_count += 1
            if filename in call_times_v2.counts_dict.keys():
                call_times_v2.counts_dict[filename].update({func.__name__: inner.calls_count})
            else:
                call_times_v2.counts_dict[filename] = {func.__name__: inner.calls_count}

            for file, func_calls_dict in call_times_v2.counts_dict.items():
                with open(file, 'w') as f:
                    for func_name, count in func_calls_dict.items():
                        f.write(f"{func_name} была вызвана {count} раза.\n")

            return func

        inner.calls_count = 0
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


@call_times_v2("res/txt/foo_v2.txt")
def foo_v2():
    pass


@call_times_v2("res/txt/foo_v2.txt")
def boo_v2():
    pass


@call_times_v2("res/txt/calls_v2.txt")
def doo_v2():
    pass


start = time.time()

# если учитывать перезапуск скрипта
if os.path.exists("res/txt/foo.txt"):
    os.remove("res/txt/foo.txt")

if os.path.exists("res/txt/calls.txt"):
    os.remove("res/txt/calls.txt")

foo()
boo()
foo()
foo()
boo()
doo()

duration = time.time() - start  # 0.0030379295349121094
print(f"v1 duration: {duration}")


start_v2 = time.time()

foo_v2()
boo_v2()
foo_v2()
foo_v2()
boo_v2()
doo_v2()

duration_v2 = time.time() - start_v2    # 0.0020003318786621094
print(f"v2 duration: {duration_v2}")

with open("res/txt/duration.txt", "a") as f:
    f.write(f" v1 {duration}\nv2 {duration_v2}\n\n")

"""
Results:
 v1 0.005245208740234375
v2 0.002819061279296875

 v1 0.004370212554931641
v2 0.008659839630126953 !!!!

 v1 0.006290912628173828
v2 0.0021741390228271484

 v1 0.003696918487548828
v2 0.0045239925384521484

 v1 0.0044858455657958984
v2 0.0022437572479248047

 v1 0.004187107086181641
v2 0.002228975296020508
"""

