"""2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50).
Выведите на экран исходный и отсортированный массивы."""

import random
size = 20
unsorted_list = [random.randint(0,50) for i in range(size)]
print(f'исходный массив\n{unsorted_list}')

def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
# находим середину и делим по ней
    middle = len(unsorted_list) // 2
    left_list = unsorted_list[:middle]
    right_list = unsorted_list[middle:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return list(merge(left_list, right_list))

# соединяем отсортированные половинки

def merge(left_half,right_half):

    res = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half) == 0:
        res = res + right_half
    else:
        res = res + left_half
    return res


print(f'отсортированный массив\n{merge_sort(unsorted_list)}')

# вариант решения Анна Марк
import random as rd

num = [i for i in range(50)]
rd.shuffle(num)
print(num)


def merge_sort(array, revers=False):
    if len(array) < 2:
        return array[:]
    sep_num = len(array) // 2
    left = merge_sort(array[:sep_num], revers=revers)
    right = merge_sort(array[sep_num:], revers=revers)
    sorted_array = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if revers:  # бонус с разворотом сортировки =))
            if left[i] > right[j]:
                sorted_array.append(left[i])
                i += 1
            else:
                sorted_array.append(right[j])
                j += 1
        else:
            if left[i] < right[j]:
                sorted_array.append(left[i])
                i += 1
            else:
                sorted_array.append(right[j])
                j += 1
    while i < len(left):
        sorted_array.append(left[i])
        i += 1
    while j < len(right):
        sorted_array.append(right[j])
        j += 1
    return sorted_array


sorted_array = merge_sort(num, revers=False)
print(sorted_array)

