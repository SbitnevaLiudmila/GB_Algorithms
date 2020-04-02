from collections import deque
# матрица смежности
g = [
    [0, 1, 1, 0, 1, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 1, 0]
]
def bfs(graph, start, finish):
    # вспомогат. список для хранения родителей для каждой вершины
    parent = [None for __ in range(len(graph))]
    is_visited = [False for __ in range(len(graph))]
    deq = deque([start])   # значение, с кот. начинаем двигаться
    is_visited[start] = True

    while len(deq) > 0:
        current = deq.pop() # берем вершину с конца очереди

        if current == finish:
            break

        for i, vertex in enumerate(graph[current]): # проходим по всем вершинам, связанным с нашей вершиной - те по строке current в нашей матрице смежности

            # vertex = 1 если есть ребро, те мы можем перейти из текущей вершины в эту
            if vertex == 1 and not is_visited[i]:
                is_visited[i] = True
                parent[i] = current
                deq.appendleft(i)
    else:
        return f'Из вершины {start} нельзя попасть в вершину {finish}'
    cost = 0
    way = deque([finish])
    i = finish
    while parent[i] != start:
        cost += 1
        way.append(parent[i])
        i = parent[i]
    cost += 1
    way.append(start)
    return f'Кратчайший путь {list(way)} длиною в {cost} условных единиц'

s = int(input('от какой вершины идти: '))
f = int(input('до какой вершины идти: '))
print(bfs(g,s,f))






# с использованием списка смежности


gr = [
    [4],
    [2, 3],
    [1, 3],
    [1, 2, 4],
    [0, 3, 9, 5],
    [4, 8, 10],
    [7, 9, 8],
    [6, 9],
    [6, 5],
    [4, 7, 6],
    [5]
]
# v это стартовая вершина
def bfs_list(v):
    dist = [float('inf')] * len(gr)
    dist[v] = 0
    q = deque([v])
    visited = [False] * len(gr)
    visited[v] = True
    while q:
        v = q.popleft()
        for x in gr[v]:
            if not visited[x]:
                visited[x] = True
                dist[x] = dist[v] + 1
                q.append(x)
    return dist

print(bfs_list(4))