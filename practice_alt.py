'''
Написати додаток, який дозволяє слідкувати за фінансами

За тиждень буду витрачати: 1000

За понеділок: 100
За вівторок: 200
...

Чи я вилетів за бюджет?
В який день я витрачав найбільше?
'''

# Ctrl C

# Поки користувач не ввів вірне число, питати нове

while True:
    try:
        weekly_budget = float(input("Please enter budget for the week: "))
        print("Entered a correct value") #!
        break
    except ValueError:
        print("Please enter a new value, this one is wrong")

print("ENd of program!")

# Monday

# Tuesday

# Wednesday