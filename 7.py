class node:

    def __init__(self):
        self.key = None
        self.left = None
        self.right = None
        self.parent = None


class binTree:

    def __init__(self):
        self.root = None
        self.nodes = {}

    def is_binTree(self, node):
        max_key = node.key
        while node.parent:
            parent = node.parent
            if parent.left == node:
                if parent.key <= max_key:
                    return False
            else:
                if parent.key > max_key:
                    return False
            max_key = max(max_key, parent.key)
            node = parent
        return True


with open('input.txt') as f:
    n = int(f.readline())
    if n <= 1:
        with open('output.txt', 'w') as f:
            f.write('CORRECT')
        exit()
    tree = binTree()
    data = []
    leaves = []
    for i in range(0, n):
        data.append(list(map(int, f.readline().split())))
        tree.nodes[i] = node()
        tree.nodes[i].key = data[i][0]
        if data[i-1][1] == -1 and data[i-1][2] == -1:
            leaves.append(i)
for i in range(0, n):
    if data[i][1] != -1:
        tree.nodes[i].left = tree.nodes[data[i][1]]
        tree.nodes[data[i][1]].parent = tree.nodes[i]
    if data[i][2] != -1:
        tree.nodes[i].right = tree.nodes[data[i][2]]
        tree.nodes[data[i][2]].parent = tree.nodes[i]
    if i == 0:
        tree.root = tree.nodes[i]

for i in leaves:
    res = tree.is_binTree(tree.nodes[i])
    if not res:
        print('INCORRECT')
        exit()
print('CORRECT')
