"""3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
Примечание: задачу можно решить без сортировки исходного массива.
Но если это слишком сложно, используйте метод сортировки,
который не рассматривался на уроках (сортировка слиянием также недопустима)."""

import random

m = 10
size = 2 * m + 1
array = random.sample(list(range(100)), size)  # генератор уникальных элементов a набора ф длиной b
print(f'исходный массив\n{array}')

# первый способ: использовала встроенный максимум и минимум, так как это не было запрещено в условиях

for i in range(len(array) // 2):
    array.remove(max(array))
    array.remove(min(array))

print(f'медиана ряда - число {array[0]}')

print('*' * 100)
# второй способ

m = 10
size = 2 * m + 1
array = random.sample(list(range(100)), size)  # генератор уникальных элементов из набора a длиной b
print(f'исходный массив\n{array}')


small_a = [0] * len(array)
large_a = [0] * len(array)

for j in range(len(array)):
    for i in range(len(array)):
        if array[i] <= array[j]:
            small_a[j] += 1
        if array[i] >= array[j]:
            large_a[j] += 1

for i in range(len(small_a)):
    if small_a[i] == large_a[i]:
        mediana_ = array[i]

print(f'медиана ряда - число {mediana_}')

