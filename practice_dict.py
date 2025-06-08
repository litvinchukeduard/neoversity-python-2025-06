week_limit = float(input('Витрати на неділю: '))

days = ["пн", "вт"]
# days = ["пн", "вт", "ср", "чт", "пт", "сб", "нд"]
expenses = {}

for day in days:
    expenses[day] = float(input(f"Витрати на {day}: "))

# {'пн': 100, 'вт': 200}

all_day = sum(expenses.values())

if all_day < week_limit:
    print(f'Залишок: {week_limit - all_day}')
else:
    print('Перевищено ліміт')

print("\nВитрати по днях:")
for day in days:
    print(f"{day}: {expenses[day]}")

# {'пн': 100, 'вт': 200, 'ср': 100}
# 'пн' -> 100
# max: 100, max_key: 'пн'

# 'вт' -> 200
# зробити перевірку
# max: 200, max_key: 'вт'

# 'ср' -> 100
# зробити перевірку
# max_value = None
# max_key = None

# for day, amount in expenses.items():
#     if amount > max_value:
#         max_value = amount
#         max_key = day

# print(max_key)
# print(max_value)

max_value = max(expenses.values())
print(max_value)

for day in expenses:
    if expenses[day] == max_value:
        print(day)
        break
