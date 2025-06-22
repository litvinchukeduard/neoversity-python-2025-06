'''
Написати додаток, який дозволяє слідкувати за фінансами

За тиждень буду витрачати: 1000

За понеділок: 100
За вівторок: 200
...

Чи я вилетів за бюджет?
В який день я витрачав найбільше?
'''

# Який планований бюджет на тиждень?
try:
    weekly_budget = float(input("Please enter budget for the week: ")) # 100.1 100
except ValueError:
    print("You have entered a wrong value, using a default value: 1000")
    weekly_budget = 1000 # TODO: clear non-numeric values

print(weekly_budget / 10)
