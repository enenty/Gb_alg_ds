"""
2). Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""
import random as rnd




def merge_sort(arr):
    if len(arr) == 1:
        return arr
    half = len(arr) // 2
    left_arr = merge_sort(arr[:half])
    right_arr = merge_sort(arr[half:])

    def merge(left_arr, right_arr):
        sorted_ = []
        i = 0
        j = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                sorted_.append(left_arr[i])
                i += 1
            else:
                sorted_.append(right_arr[j])
                j += 1
        if i < len(left_arr):
            sorted_ += left_arr[i:]
        if j < len(right_arr):
            sorted_ += right_arr[j:]
        return sorted_

    return merge(left_arr, right_arr)


MIN = 0
MAX = 100
SIZE = 10
array = [round(rnd.uniform(MIN, MAX), 2) for i in range(SIZE)]

print(array)
print(merge_sort(array))
