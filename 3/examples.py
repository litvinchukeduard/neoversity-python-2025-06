
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

# iterator = iter(my_list)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

# Iterable

# for el in (1, 2, 3):
#     ...

# print(1 + 2)

# @input_error
# def add_contact(args, book: dict):
#     name, phone, *_ = args
#     # record = book.find(name)
#     message = "Contact updated."
#     # if record is None:
#     #     record = Record(name)
#     #     book.add_record(record)
#     #     message = "Contact added."
#     #     record.add_phone(phone)
#     # if phone:
#     #     record.add_phone(phone)
#     return message

# add_contact(['John', '12321424'], {})
