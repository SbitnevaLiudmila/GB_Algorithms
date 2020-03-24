# Лучшая последовательность шагов для сортировки Шелла
# 1,4,10,23,57,132,301,701,1750

import random
size = 20
array = [random.randint(-100, 100) for __ in range(size)]
print(array)

def shell_sort(array):
    assert len(array) < 4000, 'Массив слишком большой. Используйте другую сортировку'

    def new_increment(array):
        inc = [1,4,10,23,57,132,301,701,1750]
        while len(array) <= inc[-1]:
            inc.pop()
        while len(inc) > 0:
            yield inc.pop()
    count = 0   # подсчет проходов
    for increment in new_increment(array):
        for i in range(increment,len(array)):
            for j in range(i, increment - 1, - increment):
                if array[j - increment] <= array[j]:
                    break
                array[j], array[j - increment] = array[j - increment], array[j]
                count += 1
                #print(array)
    print(count) # посмотрим количество проходов
shell_sort(array)
print(array)

# Сорт ШЕЛЛА
# Оболочка сортировки включает в себя сортировку элементов, которые находятся далеко друг от друга.
# Мы сортируем большой подсписок данного списка и продолжаем уменьшать размер списка, пока все элементы не будут отсортированы.
# Приведенная ниже программа находит разрыв, приравнивая его к половине длины списка,
# и затем начинает сортировать все элементы в нем. Затем мы продолжаем сбрасывать разрыв, пока весь список не будет отсортирован.

def shellSort(input_list):
    gap = len(input_list) // 2
    while gap > 0:

        for i in range(gap, len(input_list)):
            temp = input_list[i]
            j = i
            # Sort the sub list for this gap

            while j >= gap and input_list[j - gap] > temp:
                input_list[j] = input_list[j - gap]
                j = j - gap
            input_list[j] = temp

        # Reduce the gap for the next element

        gap = gap // 2


list = [19, 2, 31, 45, 30, 11, 121, 27]

shellSort(list)
print(list)

# еще вариант
def shell(seq):
    inc = len(seq) // 2
    while inc:
        for i, el in enumerate(seq):
            while i >= inc and seq[i - inc] > el:
                seq[i] = seq[i - inc]
                i -= inc
            seq[i] = el
        inc = 1 if inc == 2 else int(inc * 5.0 / 11)


data = [22, 7, 2, -5, 8, 4]
shell(data)
print(data)