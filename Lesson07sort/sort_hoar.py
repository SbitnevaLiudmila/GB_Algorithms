"""Альтернативный метод, впоследствии получивший название «быстрая сортировка», изобрел информатик Чарльз Хоар в 1960.
Он предполагает деление массива на две части, в одной из которых находятся элементы меньше определённого значения,
в другой – больше или равные.
Рассмотрим реализацию в Python быстрой сортировки Хоара."""
import random

def quicksort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
        s_nums = []
        m_nums = []
        e_nums = []
        for n in nums:
            if n < q:
                s_nums.append(n)
            elif n > q:
                m_nums.append(n)
            else:
                e_nums.append(n)
        return quicksort(s_nums) + e_nums + quicksort(m_nums)


# В идеале, выбранный элемент должен быть медиальным, но для его поиска пришлось бы запускать ещё один цикл.
# Наша реализация на питоне сортировки Хоара использует случайный элемент, но она тоже не идеальна:
# в случае, если выбрано первое или последнее число, а массив отсортирован,
# то на питоне быстрая сортировка будет совпадать по эффективности с пузырьковой.
#
# Впрочем, описанный алгоритм можно прокачать, сократив количество используемой памяти:


def quicksort(nums, fst, lst):
    if fst >= lst: return

    i, j = fst, lst
    pivot = nums[random.randint(fst, lst)]

    while i <= j:
        while nums[i] < pivot: i += 1
        while nums[j] > pivot: j -= 1
        if i <= j:
            nums[i], nums[j] = nums[j], nums[i]
            i, j = i + 1, j - 1
    quicksort(nums, fst, j)
    quicksort(nums, i, lst)


# В этом случае вы используете память только для организации рекурсии
# и в Python быстрая сортировка становится по - настоящему «быстрой».
# В заключении темы опишем на питоне сортировку Хоара в функциональном виде:


def quicksort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
    l_nums = [n for n in nums if n < q]

    e_nums = [q] * nums.count(q)
    b_nums = [n for n in nums if n > q]
    return quicksort(l_nums) + e_nums + quicksort(b_nums)