import sys
'''
Написати додаток, схожий на cat
cat hello.txt

python3 2/cat.py hello.txt
'''

# 1. Отримати шлях до файлу
print(sys.argv)

if len(sys.argv) != 2:
    print("Please provide file path!")
    sys.exit() # Або просто exit()

file_path = sys.argv[1]
# file = open()
with open(file_path) as file:
    #for line in file.readlines(): # Читає усі рядки з файлу.
    for line in file: # Читати по одному рядку
        # print(line.rstrip())
        print(line, end='')
