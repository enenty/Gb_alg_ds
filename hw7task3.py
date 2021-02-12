"""
3). Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части:
в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
"""

import random as rnd

MIN = -1000
MAX = 1000
SIZE = (2 * rnd.randint(5, 10)) + 1
array = [rnd.randint(MIN, MAX) for i in range(SIZE)]

# array = [15, 92, 32, 32, 32, 32, 32, 87, 27, 30, 19]
# array = [8, 4, 4, 4, 0]

print(f'{array} изначальный массив')
print(f'{sorted(array)} отсортированный массив для наглядности')


def median(arr):
    for i in range(len(array)):
        count_more = 1
        count_less = 1
        quantity = 0
        for el in array:
            if array[i] > el:
                count_less += 1
            if array[i] < el:
                count_more += 1
            if array[i] == el:
                 quantity += 1
        if count_less == count_more:
            return array[i]
        if (count_less == len(array) // 2) and quantity == (count_less) // 2:
            return array[i]
        if (count_more == len(array) // 2) and quantity == (count_more) // 2:
            return array[i]
        if quantity == count_less + count_more:
            return array[i]
        if abs(count_less - quantity) == abs(count_more - quantity):
            return array[i]
        if quantity >= len(array)//2:
            return array[i]


print(median(array))

