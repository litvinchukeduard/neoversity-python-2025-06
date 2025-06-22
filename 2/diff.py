# from cat import 

import sys
from itertools import zip_longest

from colorama import Fore, Back, Style
'''
Потрібно написати схожий додаток на diff

Зробимо основний функціонал, порівняння двох файлів

diff a.txt b.txt

python3 2/diff.py a.txt b.txt
'''

def compare_two_files(file_one_path: str, file_two_path: str):

    '''
    1. Відкрити файл

    2. Проситати усі рядки з файлу у список

    3. Порівняти списки рядки
    '''

    with open(file_one_path) as file:
        file_one_lines_list = file.readlines()

    with open(file_two_path) as file:
        file_two_lines_list = file.readlines()

    # print(file_one_lines_list)
    # print(file_two_lines_list)

    for number, (file_one_line, file_two_line) in enumerate(zip_longest(file_one_lines_list, file_two_lines_list, fillvalue='')):
        if file_one_line != file_two_line:
            print(f'Line number: {number + 1}')
            print(f'{Fore.RED}< {file_one_line.rstrip()}{Style.RESET_ALL}')
            print(f'{Fore.GREEN}> {file_two_line.rstrip()}{Style.RESET_ALL}')
            print()
    
    # for i in range(len(file_one_lines_list)):
    #     file_one_line = file_one_lines_list[i].rstrip()
    #     file_two_line = file_two_lines_list[i].rstrip()

    #     if file_one_line != file_two_line:
    #         print(f'Line number: {i + 1}')
    #         print(f'< {file_one_line}')
    #         print(f'> {file_two_line}')
    #         print()


def main():
    if len(sys.argv) != 3:
        print("Please provide file one path and file two path!")
        sys.exit() # Або просто exit()

    # file_one = sys.argv[1]
    # file_two = sys.argv[2]
    _, file_one, file_two = sys.argv

    compare_two_files(file_one, file_two)

main()
