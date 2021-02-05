"""
Проанализировать скорость и сложность одного любого алгоритма
из разработанных в рамках домашнего задания первых трех уроков.
Урок 3. Задача 4.
Определить, какое число в массиве встречается чаще всего.
"""

import timeit
import cProfile
import random as rnd


def find_most_frequent(array):
    max_freq = array[0]
    max_count = 1
    for i in array:
        count = 0
        for num in range(len(array)):
            if i == array[num]:
                count += 1
            if count > max_count:
                max_count = count
                max_freq = i
    return f'{max_freq} имеет {max_count} совпадений(я)'


size = 10
for i in range(3):
    MIN_ITEM = 0
    MAX_ITEM = 100
    array = [rnd.randint(MIN_ITEM, MAX_ITEM) for _ in range(size)]
    print(timeit.timeit('find_most_frequent(array)', number=1000, globals=globals()))
    size = size * 10

# size = 10      0.009418299999999998
# size = 100     0.624103
# size = 1000    70.68730670000001
#
# O(n**2)

cProfile.run('find_most_frequent(array)')

# 1004 function calls in 0.068 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.068    0.068 <string>:1(<module>)
#         1    0.068    0.068    0.068    0.068 task1.py:20(find_most_frequent)
#         1    0.000    0.000    0.068    0.068 {built-in method builtins.exec}
#      1000    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


#########################################################

def most_frequent_dict(array):#
    max_freq = 1
    num = None
    count_dict = {}
    for item in array:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
        if count_dict[item] > max_freq:
            max_freq = count_dict[item]
            num = item
    if num is not None:
        return f'{num} имеет {max_freq} совпадений(я)'
    else:
        return f'Все элементы уникальны'

size = 10
for i in range(3):
    MIN_ITEM = 0
    MAX_ITEM = 100
    array = [rnd.randint(MIN_ITEM, MAX_ITEM) for _ in range(size)]
    print(timeit.timeit('most_frequent_dict(array)', number=1000, globals=globals()))
    size = size * 10

# size = 10 0.001174399999999999
# size = 100 0.011460499999999998
# size = 1000 0.1163548
#
# O(n)

cProfile.run('most_frequent_dict(array)')

# 4 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task1.py:64(most_frequent_dict)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


#########################################################


def count_number(array):
    max_count = 1
    max_number = None
    for number in array:
        num_count = array.count(number)
        if num_count > max_count:
            max_count = num_count
            max_number = number
    if max_number is None:
        return f'Все элементы уникальны'
    else:
        return f'{max_number} имеет {max_count} совпадений(я)'

size = 10
for i in range(3):
    MIN_ITEM = 0
    MAX_ITEM = 100
    array = [rnd.randint(MIN_ITEM, MAX_ITEM) for _ in range(size)]
    print(timeit.timeit('count_number(array)', number=1000, globals=globals()))
    size = size * 10

# size = 10    0.001940399999999995
# size = 100   0.1448112
# size = 1000  13.593671299999999
#
# O(n**2)
#
cProfile.run('count_number(array)')
# 1004 function calls in 0.014 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.014    0.014 <string>:1(<module>)
#         1    0.000    0.000    0.014    0.014 task1.py:110(count_number)
#         1    0.000    0.000    0.014    0.014 {built-in method builtins.exec}
#      1000    0.014    0.000    0.014    0.000 {method 'count' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}



######################## Вывод #########################

# Асимптоматика 1 и 3 вариантов имеет квадратичную сложность.
# Кроме того, в обоих случаях применяются стандартные функции,
# len() для 1 варианта и count() для 3 варианта, которые вызываются
# в линейной зависимости от размера массива, что сильно замедляет работу алгоритма.
# 2 вариант имеет линейную сложность и является самым удачным за счет хранения промежуточных данных в словаре.
