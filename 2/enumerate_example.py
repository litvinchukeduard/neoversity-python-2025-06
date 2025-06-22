from itertools import zip_longest

my_list = ['a', 'b', 'c', 'd']
my_list_two = ['x', 'y', 'z']

# for pair in enumerate(zip(my_list, my_list_two)):
#     print(pair)

for number, (first_list_element, second_list_element) in enumerate(zip_longest(my_list, my_list_two, fillvalue='Hello')):
    print(number, first_list_element, second_list_element)
    # print(first_list_element)
    # print(second_list_element)
    
