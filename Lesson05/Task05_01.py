"""Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за четыре квартала для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий,
чья прибыль выше среднего и ниже среднего."""

from collections import namedtuple

Firm = namedtuple('Firm', 'name q_1 q_2 q_3 q_4 year')
num = int(input('введите количество предприятий: '))
firm = [0 for __ in range(num)]
sum_allfirms = 0
for i in range(num):
    name = (input(f'введите название {i+1}-й фирмы: '))
    q_1 = float(input('прибыль 1 кв: '))
    q_2 = float(input('прибыль 2 кв: '))
    q_3 = float(input('прибыль 3 кв: '))
    q_4 = float(input('прибыль 4 кв: '))
    year = q_1 + q_2 + q_3 + q_4
    sum_allfirms += year
    firm[i] = Firm(name, q_1, q_2, q_3, q_4, year)


av_profit = sum_allfirms / num
print(f'Средняя годовая прибыль равна: {av_profit:.2f}')
firms_over = []
firms_below = []

for i in range(num):
    if firm[i].year > av_profit:
        firms_over.append(firm[i].name)
    elif firm[i].year < av_profit:
        firms_below.append(firm[i].name)

print(f'Список предприятий с прибылью выше средней:')
print(*firms_over)
print(f'Список предприятий с прибылью ниже средней:')
print(*firms_below)