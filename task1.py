"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""

from collections import Counter

comp_cnt = Counter()
comp_num = int(input('Введите количество компаний: '))


for comp in range(comp_num):
    comp_name = input(f'Введите название {comp + 1} компании: ')
    for quart in range(4):
        comp_cnt[comp_name] += float(input(f'Введите прибыль за {quart + 1} квартал'))

avg_profit = sum(comp_cnt.values()) / comp_num
print(f'Средняя прибыль предприятий за год: {avg_profit:.2f}')

print('Доход ниже среднего у компаний:')
for comp, profit in comp_cnt.items():
    if profit < avg_profit:
        print(f'{comp}')

print('Доход выше среднего у компаний:')
for comp, profit in comp_cnt.items():
    if profit > avg_profit:
        print(f'{comp}')









