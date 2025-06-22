'''
написати рекурсивну функцію, яка буде рахувати суму

10 -> 10 + 9 + 8 + ... + 

10 -> 10 + sum_numbers(9)
9 -> 9 + sum_numbers(8)
...

1 -> 1 + ... = 1
'''

def sum_numbers(number: int) -> int: # Can't even fix with tail-recursion
    # Умова коли вона зупиняється
    if number == 1:
        return 1

    # Рекурсивний крок
    result = number + sum_numbers(number - 1)

    # Повернення результату
    return result

try: 
    print(sum_numbers(1000))
except RecursionError:
    print("Ми заповнили стек для рекурсії")
