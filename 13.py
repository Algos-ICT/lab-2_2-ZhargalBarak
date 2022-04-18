from collections import deque

class node:

    def __init__(self):
        self.key = None
        self.left = None
        self.right = None
        self.parent = None
        self.height = 0
        self.balance = None


class binTree:

    def __init__(self):
        self.root = None
        self.nodes = {}

    def set_height(self, node):
        node.height = 1
        while node.parent:
            parent = node.parent
            if parent.height <= node.height:
                parent.height = node.height + 1
            else:
                break
            node = parent

    def set_balance(self):
        for i in range(1, n + 1):
            node = self.nodes[i]
            if node.left:
                if node.right:
                    node.balance = node.right.height - node.left.height
                else:
                    node.balance = -node.left.height
            else:
                if node.right:
                    node.balance = node.right.height
                else:
                    node.balance = 0

    def left_turn(self, A):
        B = A.right
        if B.balance == -1:
            C = B.left
            X = C.left
            Y = C.right
            if X:
                X.parent = A
            A.right = X
            if Y:
                Y.parent = B
            B.left = Y
            if A.key != self.root.key:
                C.parent = A.parent
                if A.parent.left == A:
                    A.parent.left = C
                else:
                    A.parent.right = C
            else:
                self.root = C
            A.parent = C
            C.left = A
            B.parent = C
            C.right = B
        else:
            Y = B.left
            if Y:
                Y.parent = A
            A.right = Y
            if A != self.root:
                B.parent = A.parent
                if A.parent.left == A:
                    A.parent.left = B
                else:
                    A.parent.right = B
            else:
                self.root = B
            A.parent = B
            B.left = A

    def tree_output(self):
        q = deque()
        q.append(self.root)
        i = 1
        with open('output.txt', 'w') as f:
            global n
            f.write(str(n) + '\n')
            while len(q) != 0:
                node = q.popleft()
                f.write(str(node.key))
                if node.left:
                    i += 1
                    f.write(' ' + str(i))
                    q.append(node.left)
                else:
                    f.write(' 0')
                if node.right:
                    i += 1
                    f.write(' ' + str(i) + '\n')
                    q.append(node.right)
                else:
                    f.write(' 0\n')




with open('input.txt') as f:
    n = int(f.readline())
    tree = binTree()
    data = []
    leaves = []
    for i in range(1, n+1):
        data.append(list(map(int, f.readline().split())))
        tree.nodes[i] = node()
        tree.nodes[i].key = data[i-1][0]
        if data[i-1][1] == 0 and data[i-1][2] == 0:
            leaves.append(i)


for i in range(1, n+1):
    if data[i-1][1] != 0:
        tree.nodes[i].left = tree.nodes[data[i-1][1]]
        tree.nodes[data[i-1][1]].parent = tree.nodes[i]
    if data[i-1][2] != 0:
        tree.nodes[i].right = tree.nodes[data[i-1][2]]
        tree.nodes[data[i-1][2]].parent = tree.nodes[i]
    if i == 1:
        tree.root = tree.nodes[i]

for i in leaves:
    tree.set_height(tree.nodes[i])

tree.set_balance()
tree.left_turn(tree.root)
tree.tree_output()