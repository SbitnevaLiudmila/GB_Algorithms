"""Шейкерная сортировка :: Shaker sort
(Коктейльная сортировка :: Cocktail sort)
Разновидность пузырька. На первом проходе как обычно — задвигаем максимум в конец.
Потом резко разворачиваемся и толкаем минимум в начало.
Отсортированные крайние области массива увеличиваются в размерах после каждой итерации."""


def shaker(data):
    up = range(len(data) - 1)
    print(up)
    print(reversed(up))

    while True:
        for indices in (up, reversed(up)):  # up - перебор от 0 до последнего элемента, reversed - наоборот, те сначала перебор с одну сторону, потом в другую
            swapped = False
            for i in indices:
                if data[i] > data[i + 1]:
                    data[i], data[i + 1] = data[i + 1], data[i]
                    swapped = True
            if not swapped:
                return data

list_ = [19, 2, 31, 45, 30, 11, 121, 27]
shaker(list_)
print(list_)



