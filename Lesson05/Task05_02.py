"""Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Примечание: Если воспользоваться функциями hex() и/или int() для преобразования систем счисления,
задача решается в несколько строк. Для прокачки алгоритмического мышления такой вариант не подходит.
Поэтому использование встроенных функций для перевода из одной системы счисления в другую в данной задаче под запретом.
Вспомните начальную школу и попробуйте написать сложение и умножение в столбик."""

# Десятичные	    0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16
# Шестнадцатеричные	0	1	2	3	4	5	6	7	8	9	A	B	C	D	E	F	10

from collections import deque
# сначала сложение, аргументы приходят в виде строки
def sum_16(first, second):
    first = first.upper()
    second = second.upper()
    if len(second) > len(first):  # более длинное число ставим первым
        first, second = list(second), list(first) # и преобразуем в список
    else:
        first, second = list(first), list(second)
    # сделано все в одном словаре, чтобы только на него ссылаться и при переводе из 10 в 16 и обратно
    dict10_16 = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
               '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
               0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
               8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    result = deque()
    adding = 0
    while first:
        if second:
            spam = dict10_16[first.pop()] + dict10_16[second.pop()] + adding
        else:
            spam = dict10_16[first.pop()] + adding
        result.appendleft(dict10_16[spam % 16])
        adding = spam // 16
    if adding != 0:
        result.appendleft(dict10_16[adding]) # если при последнем сложении увеличивается разряд
    return result

print(*sum_16('FFFF','C4'), sep='') # проверка работы функции

print('*' * 50)

# теперь умножение

first = 'FFfFF'
second = 'eEE'
first = first.upper()
second = second.upper()
if len(second) > len(first):  # более длинное число ставим первым
    first, second = list(second), list(first)
else:
    first, second = list(first), list(second)

dict10_16 = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
           '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
            0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
            8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

result = [deque() for _ in range(len(second))]  # задаем пустую очередь для записи промежуточного результата
adding = 0
res_mult = [0]   # список для окончательного результата
temp_second = second.copy()
for i in range(len(second)):  # внешний цикл - перебор по короткому числу, внутренний по длинному
    temp_first = first.copy()
    m = dict10_16[temp_second.pop()] # отрезаем последнюю цифру с конца
    adding = 0
    while temp_first:
        res1 = dict10_16[temp_first.pop()] * m + adding
        result[i].appendleft(dict10_16[res1 % 16])
        adding = res1 // 16
    if adding != 0:
        result[i].appendleft(dict10_16[adding])
    for q in range(i):   # добиваем справа нулями, для смещения разряда
        result[i].append(dict10_16[0])
    res_mult = sum_16(''.join([str(x) for x in list(res_mult)]), ''.join(list(result[i]))) # переводим все в строку, так как
                                                                                           # функция сложения принимает аргументы в виде строки
print(*res_mult, sep='')





