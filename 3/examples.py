
my_list = [1, 2, 3]

my_list += {4, 5, 6}

print(my_list)

def my_func():
    for i in range(5):
        yield i

# generator = my_func()
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))

iterator = iter(my_list)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))

# Iterable

# for el in (1, 2, 3):
#     ...

# print(1 + 2)