"""2. Доработать алгоритм Дейкстры (рассматривался на уроке),
чтобы он дополнительно возвращал список вершин, которые необходимо обойти."""

g = [
    [0, 0, 1, 1, 9, 0, 0, 0],
    [0, 0, 9, 4, 0, 0, 5, 0],
    [0, 9, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 8, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 2, 0]
]
# первая - часть - алгоритм Дейкстры с урока

def dijkstra(graph, start):
    # цена каждой вершины пока везде бесконечность
    cost = [float('inf')] * len(g)
    # родительская вершина поке везде -1 как нереальная цифра
    parent = [-1] * len(g)
    # пока список вершин, для всех ложь(не посещали)
    is_visited = [False] * len(g)
    # цена стартовой вершины - 0 так там мы уже находимся
    cost[start] = 0
    min_cost = 0
    # пока min_cost меньше бесконечности, обходим граф в цикле
    while min_cost < float('inf'):
        is_visited[start] = True  # так как мы ее посетили
        for i, vertex in enumerate(graph[start]):  # перебираем каждую строку графа, начинаем со стартовой, те с нулевой
            if vertex != 0 and not is_visited[i]:  # если ребро(vertex) не равно 0, те ребро есть и мы ее не посещали
                if cost[i] > vertex + cost[start]:  # если (сумма ребра и цены стартовой вершины) меньше текущей цены вершины, а она меньше так как цена бесконечность для новой вершины
                    cost[i] = vertex + cost[start]  # присваиваем цене тек. вершины = ребро + цену стартовой вершины
                    parent[i] = start  # родитель текущей вершины становится стартом

        min_cost = float('inf')  # самое большое число тк мы ищем минимум
        for i in range(len(g)):  # ищем минимум из полученных цен ребер
            if min_cost > cost[i] and not is_visited[i]:
                min_cost = cost[i]
                start = i  # стартом становится i-тая вершина
    return cost, parent

# добавила в return parent, так как parent и есть нужный нам список для возвращения пути к каждой вершине
# осталось только из него составить пути
def restore_path(v):
    if parent[v] == -1:  # случай, когда есть вершины, в которые невозможно попасть
        return []
    path = [v] # сначала в списке конечная вершина
    while v > 0:
        v = parent[v]  # от рассмотрения вершины переходим к ее предку, сделав это несколько раз, получим целый путь
        path.append(v) # добавляем ее в путь
    path.reverse()
    return path

s = int(input('от какой вершины идти: '))
cost, parent = dijkstra(g, s)
for i in range(1, len(g)):
    print(f'путь в вершину номер {i}: {restore_path(i)}')