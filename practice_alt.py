'''
Написати додаток, який дозволяє слідкувати за фінансами

За тиждень буду витрачати: 1000

За понеділок: 100
За вівторок: 200
...

Чи я вилетів за бюджет?
В який день я витрачав найбільше?
'''

# Tab - to move right
# Shift Tab - to move left
def try_getting_number_from_user(prompt):
    while True:
        try:
            weekly_budget = float(input(prompt))
            # print("Entered a correct value") #!
            return weekly_budget
        except ValueError:
            print("Please enter a new value, this one is wrong")

# Ctrl C

# Поки користувач не ввів вірне число, питати нове

# Ctr / або Command /
# while True:
#     try:
#         weekly_budget = float(input("Please enter budget for the week: "))
#         print("Entered a correct value") #!
#         break
#     except ValueError:
#         print("Please enter a new value, this one is wrong")

# print("ENd of program!")

weekly_budget = try_getting_number_from_user("Please enter budget for the week: ")
# print("Budget for the week is " + weekly_budget)
print(f"Budget for the week is {weekly_budget}")

# list, tuple, dict, set

# {100, 200, 300} -> No order, not recommended

# l = [100, 200, 300] l[0] - Monday, l[1]- Tuesday - Recommended

# t = (100, 200, 300) -> Not recommended, fixed value

# d = {0: 100, 1: 200}
# spendings = {'Monday': 100, 'Tuesday': 200}

money_spent_during_the_week = []

# Monday
money_spent_during_the_week.append(try_getting_number_from_user("Please enter money spent on Monday: "))
# Tuesday
money_spent_during_the_week.append(try_getting_number_from_user("Please enter money spent on Monday: "))
# Wednesday
money_spent_during_the_week.append(try_getting_number_from_user("Please enter money spent on Monday: "))

print(money_spent_during_the_week)

# spending = (monday_money_spent, tuesday_money_spent, wednesday_money_spent)
