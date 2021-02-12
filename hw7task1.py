"""
1). Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
Примечания:
● алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
● постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.

 Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.
"""
import random as rnd


def bubble_desc(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


MIN = -100
MAX = 100
SIZE = 10
array = [rnd.randint(MIN, MAX) for i in range(SIZE)]
print(array)
print(bubble_desc(array))
