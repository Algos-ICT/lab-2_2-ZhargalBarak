class node:

    def __init__(self):
        self.key = None
        self.left = None
        self.right = None
        self.parent = None
        self.passed = None


class binTree:

    def __init__(self):
        self.root = None
        self.nodes = {}

    def is_binTree(self):
        node = self.root
        prev = None
        next = None
        while True:
            if node.left and not node.left.passed:
                node = node.left
            elif node.right and not node.right.passed:
                if not prev:
                    prev = node
                elif not next:
                    next = node
                else:
                    prev = next
                    next = node
                if next:
                    if prev.key >= next.key and prev.right != next:
                        return False
                    elif prev.key > next.key and prev.right == next:
                        return False
                node.passed = True
                node = node.right
            else:
                if not node.passed:
                    if not prev:
                        prev = node
                    elif not next:
                        next = node
                    else:
                        prev = next
                        next = node
                    if next:
                        if prev.key >= next.key and prev.right != next:
                            return False
                        elif prev.key > next.key and prev.right == next:
                            return False
                node.passed = True
                if node != self.root:
                    while node.passed:
                        node = node.parent
                        if node == self.root:
                            break
                else:
                    break
        return True


with open('input.txt') as f:
    n = int(f.readline())
    if n <= 1:
        with open('output.txt', 'w') as f:
            f.write('CORRECT')
        exit()
    tree = binTree()
    data = []
    for i in range(0, n):
        data.append(list(map(int, f.readline().split())))
        tree.nodes[i] = node()
        tree.nodes[i].key = data[i][0]

for i in range(0, n):
    if data[i][1] != -1:
        tree.nodes[i].left = tree.nodes[data[i][1]]
        tree.nodes[data[i][1]].parent = tree.nodes[i]
        if tree.nodes[i].left.key >= tree.nodes[i].key:
            with open('output.txt', 'w') as f:
                f.write('INCORRECT')
                exit()
    if data[i][2] != -1:
        tree.nodes[i].right = tree.nodes[data[i][2]]
        tree.nodes[data[i][2]].parent = tree.nodes[i]
        if tree.nodes[i].key > tree.nodes[i].right.key:
            with open('output.txt', 'w') as f:
                f.write('INCORRECT')
                exit()
    if i == 0:
        tree.root = tree.nodes[i]

res = tree.is_binTree()
if res == True:
    print('CORRECT')
else:
    print('INCORRECT')