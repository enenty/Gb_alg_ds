"""
1) Определение количества различных подстрок с использованием хеш-функции.
Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.
Пример работы функции:

func("papa")
6
func("sova")
9
"""

import hashlib


def get_substring(inp_string):
    result = []
    hash_list = []
    for i in range(len(inp_string) + 1):
        for j in range(i + 1, len(inp_string) + 1):
            if inp_string == inp_string[i:j]:
                continue
            result.append(hashlib.sha1(inp_string[i:j].encode('utf-8')).hexdigest())
    for substr in result:
        if substr not in hash_list:
            hash_list.append(substr)
    print(hash_list)
    return len(hash_list)


inp_string = input('Введите строку: ')
print(f'Количество уникальных подстрок в строке {inp_string}:\n{get_substring(inp_string)}')
