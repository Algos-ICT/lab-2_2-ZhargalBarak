from collections import deque

class node:

    def __init__(self):
        self.key = None
        self.left = None
        self.right = None
        self.parent = None
        self.iter = None


class binTree:

    def __init__(self):
        self.root = None
        self.nodes = {}

    def delete_node_with_all(self, key):
        if key in self.nodes:
            root = self.nodes[key]
            if root.parent.left == root:
                root.parent.left = None
            else:
                root.parent.right = None
            delete_list = deque()
            delete_list.append(root)
            while len(delete_list) != 0:
                node = delete_list.popleft()
                if node.left:
                    delete_list.append(node.left)
                if node.right:
                    delete_list.append(node.right)
                self.nodes.pop(node.iter)
            global f
            f.write(str(len(self.nodes)) + '\n')

with open('input.txt') as f:
    n = int(f.readline())
    tree = binTree()
    data = []
    nodes_iter = {}
    for i in range(1, n+1):
        data.append(list(map(int, f.readline().split())))
        tree.nodes[i] = node()
        tree.nodes[i].key = data[i-1][0]
        tree.nodes[i].iter = i
        nodes_iter[data[i-1][0]] = i
    m = int(f.readline())
    for_delete = list(map(int, f.readline().split()))


for i in range(1, n+1):
    if data[i-1][1] != 0:
        tree.nodes[i].left = tree.nodes[data[i-1][1]]
        tree.nodes[data[i-1][1]].parent = tree.nodes[i]
    if data[i-1][2] != 0:
        tree.nodes[i].right = tree.nodes[data[i-1][2]]
        tree.nodes[data[i-1][2]].parent = tree.nodes[i]
    if i == 1:
        tree.root = tree.nodes[i]


with open('output.txt', 'w') as f:
    for j in for_delete:
        if j in nodes_iter:
            j = nodes_iter[j]
        else:
            j = 0
        if j in tree.nodes:
            tree.delete_node_with_all(j)
        else:
            f.write(str(len(tree.nodes)) + '\n')

