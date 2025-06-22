# Якщо є set, list або tuple, str
import colorama

my_list = {'a', 'b', 'c'}
# my_list = "abc"

for el in my_list:
    ...

_, value_two, value_three = my_list

# value_one = my_list[1]
# value_two = my_list[2]

# print(value_one)
print(value_two)
print(value_three)

# from colorama import Fore, Back, Style
# print(Fore.RED + 'some red text')
# print(Back.GREEN + 'and with a green background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')