"""3. Написать программу, которая обходит не взвешенный ориентированный граф без петель,
в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
Примечания:
a. граф должен храниться в виде списка смежности;
b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин."""

# первая функция генерирует граф
# массив connected сделан для того, чтобы граф был связанным
import random

def gen_graph(number):
    gr = []
    connected = [0]
    for i in range(number):
        list_ = list(range(number))
        list_.remove(i)
        len_ = random.randint(0, number - 1)
        vertex = random.sample(list_, len_)
        if i in connected:
            for x in vertex:
                connected.append(x)
        else:
            for x in vertex:
                if x in connected:
                    break
            else:
                vertex.append(random.choice(connected))
            connected.append(i)
            for x in vertex:
                connected.append(x)
        gr.append(vertex)
    return gr

n = int(input('введите количество вершин: '))
graph = gen_graph(n)
print(graph)

is_visited = [False] * len(graph)
def dfs(v):
    is_visited[v] = True
    print((is_visited))
    for x in graph[v]:
        if not is_visited[x]:
            dfs(x)
ver = int(input('введите с какой вершины начать обход: '))

dfs(ver)

