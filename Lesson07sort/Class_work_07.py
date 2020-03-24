"""
начало классной работы
пузырек и модификация
"""
import random
# size = 10
# array = [i for i in range(size)]
# random.shuffle(array)
# print(array)

# Простой вариант пузырька
def bubble_sort_simple(array):
    for j in range(len(array) - 1):
        for i in range(len(array) - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
# вариант улучшенный
# Представим себе, что у нас есть массив на два миллиона чисел, и мы уже сделали миллион проходов.
# Это значит, что как минимум миллион чисел в массиве уже стоят на своих законных местах в конце массива.
# Следовательно, нет никакого смысла проходить правую половину массива, потому что там никаких изменений точно уже не будет.
# Итак, если на первом проходе мы делаем N-1 сравнение, то на втором достаточно N-2,
# на третьем  достаточно N-3 и так далее по мере увеличения количества чисел, которые стоят на своих местах.

# !!!Но по проведенному анализу в файле test он не тратит меньше времени
def bubble_sort_improved(array):
    for j in range(len(array) - 1):
        for i in range(len(array) - 1 - j):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
        print(array)

size = 10
array = [i for i in range(size)]
random.shuffle(array)
print(array)
bubble_sort_improved(array)
print(array)
print('*******************')
# Количество операций (а вместе с ним и время работы) нам удалось сократить вдвое.
# Хотя, следует признать, что оценка времени работы алгоритма все еще составляет .
# Второе соображение для оптимизации метода простого обмена основано на таком утверждении: если за полный проход
# в массиве не сделано ни одной перестановки, то его можно считать отсортированным.
# Что значит «не сделано ни одной перестановки»? Это значит, что все пары соседних чисел расположены «правильно»,
# то есть большее число идет позже меньшего, поэтому они в перестановках не нуждаются.
# Это позволяет значительно сократить время в случаях, когда более или менее повезло с исходными данными.
# Например, в массиве 8, 1, 2, 3, 4, 5, 6 будет вообще достаточно одного прохода, чтобы вытолкнуть восьмерку на последнее место.
# Существенных изменений в структуре программы не будет – как был двойной цикл, так и остался.
# Просто внешний цикл будет заменен на цикл с условием.
n = 1
not_in_order = True
while not_in_order:
    not_in_order = False
    for i in range(len(array) - n):  # минус n так как i+1 (иначе ошибка будет)
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
            not_in_order = True  # так как пришлось переставлять
    n += 1
    print(array)
print(array)
print('**************')


def bubblesort_improved_2(array):
    j = len(array) - 1
    not_in_order = True
    while not_in_order:
        not_in_order = False
        for i in range(j):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                not_in_order = True
        j -= 1
        print(array)

array1 = [i for i in range(size)]
random.shuffle(array1)
print(array1)
bubblesort_improved_2(array1)
print(array1)

def bubble_sort(nums):
    # Устанавливаем swapped в True, чтобы цикл запустился хотя бы один раз
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Меняем элементы
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Устанавливаем swapped в True для следующей итерации
                swapped = True

# Проверяем, что оно работает
random_list_of_nums = [5, 2, 1, 8, 4]
bubble_sort(random_list_of_nums)
print(random_list_of_nums)



