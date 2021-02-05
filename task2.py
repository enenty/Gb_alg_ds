"""
Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""
from collections import deque

HEX = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
       'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
       0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
       10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}


def sum_hex(hex1, hex2):
    addition = 0
    sum_deque = deque()
    if len(hex1) < len(hex2):
        hex1, hex2 = hex2, hex1
        while len(hex1) != len(hex2):
            hex2.extendleft('0')
    if len(hex1) > len(hex2):
        while len(hex1) != len(hex2):
            hex2.extendleft('0')
    for i in range(len(hex1)):
        last1_hex = hex1.pop()
        last2_hex = hex2.pop()
        last1 = [i for i in HEX if HEX[i] == last1_hex].pop()
        last2 = [i for i in HEX if HEX[i] == last2_hex].pop()
        sum_ = last1 + last2 + addition
        if sum_ >= 16:
            sum_ = sum_ - 16
            addition = 1
            last_sum = [i for i in HEX if HEX[i] == sum_].pop()
            sum_deque.append(last_sum)
        else:
            addition = 0
            sum_ = [i for i in HEX if HEX[i] == sum_].pop()
            sum_deque.append(sum_)
    if addition == 1:
        sum_deque.append('1')
    sum_deque.reverse()

    return f'Сумма чисел равна {"".join(list(sum_deque))}'


hex1 = deque(input('Введите первое шестнадцатеричное число: '))
hex2 = deque(input('Введите второе шестнадцатеричное число: '))


print((sum_hex(hex1, hex2)))

