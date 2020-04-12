

class Node:
    def __init__(self, w=None, l=None, r=None, s=None):
        self.weight = w
        self.left = l
        self.right = r
        self.symb = s

    def __lt__(self, other):
        return self.weight < other.weight

def go(node, path):
    if not (node.symb is None):
        global paths
        paths[node.symb] = path
        return
    go(node.left, path + [0])
    go(node.right, path + [1])

data = 'abra cadabra'
data = data.lower()
objects = set(data)
counts = []
for i in objects:
  counts.append(data.count(i))
leaves_list = list(zip(objects, counts))
nodes = [Node(x[1], None, None, x[0]) for x in leaves_list]
while len(nodes) > 1:
    nodes.sort()
    nodes.append(Node(nodes[0].weight + nodes[1].weight, nodes[0], nodes[1], None))
    nodes.pop(0)
    nodes.pop(0)
paths = {}
go(nodes[0], [])
print(paths)
s = []
for x in data:
    s += map(str, paths[x])
s = ''.join(s)
print(s)