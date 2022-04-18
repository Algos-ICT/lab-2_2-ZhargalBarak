class node:

    def __init__(self):
        self.key = None
        self.left = None
        self.right = None
        self.parent = None
        self.passed = False


class binTree:

    def __init__(self):
        self.root = None
        self.nodes = {}

    def in_order(self):
        node = self.root
        passed = not node.passed
        while True:
            if node.left and node.left.passed != passed:
                node = node.left
            elif node.right and node.right.passed != passed:
                print(node.key, end=' ')
                node.passed = passed
                node = node.right
            else:
                if node.passed != passed:
                    print(node.key, end=' ')
                    node.passed = passed
                if node != self.root:
                    while node.passed == passed:
                        node = node.parent
                        if node == self.root:
                            break
                else:
                    break

    def pre_order(self):
        node = self.root
        passed = not node.passed
        while True:
            if node.left:
                if node.left.passed != passed:
                    print(node.key, end=' ')
                    node = node.left
                elif node.right and node.right.passed != passed:
                    node = node.right
                else:
                    node.passed = passed
                    if node == self.root:
                        break
                    else:
                        node = node.parent
            else:
                if node.right:
                    if node.right.passed != passed:
                        print(node.key, end=' ')
                        node = node.right
                    else:
                        node.passed = passed
                        if node == self.root:
                            break
                        else:
                            node = node.parent
                else:
                    print(node.key, end=' ')
                    node.passed = passed
                    if node == self.root:
                        break
                    else:
                        node = node.parent

    def post_order(self):
        node = self.root
        passed = not node.passed
        while True:
            if node.left:
                if node.left.passed != passed:
                    node = node.left
                elif node.right and node.right.passed != passed:
                    node = node.right
                else:
                    print(node.key, end=' ')
                    node.passed = passed
                    if node == self.root:
                        break
                    else:
                        node = node.parent
            else:
                if node.right:
                    if node.right.passed != passed:
                        node = node.right
                    else:
                        print(node.key, end=' ')
                        node.passed = passed
                        if node == self.root:
                            break
                        else:
                            node = node.parent
                else:
                    print(node.key, end=' ')
                    node.passed = passed
                    if node == self.root:
                        break
                    else:
                        node = node.parent



with open('input.txt') as f:
    n = int(f.readline())
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
    if data[i][2] != -1:
        tree.nodes[i].right = tree.nodes[data[i][2]]
        tree.nodes[data[i][2]].parent = tree.nodes[i]
    if i == 0:
        tree.root = tree.nodes[i]

tree.in_order()
print()
tree.pre_order()
print()
tree.post_order()
