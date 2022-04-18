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

    def insert(self, key):
        if key not in self.nodes:
            self.nodes[key] = node()
            self.nodes[key].key = key
            if not tree.root:
                tree.root = self.nodes[key]
            else:
                root = tree.root
                while True:
                    if key < root.key:
                        if not root.left:
                            root.left = self.nodes[key]
                            self.nodes[key].parent = root
                            break
                        else:
                            root = root.left
                    else:
                        if not root.right:
                            root.right = self.nodes[key]
                            self.nodes[key].parent = root
                            break
                        else:
                            root = root.right

    def findMinMore(self, key):
        min = float('inf')
        for j in self.nodes:
            if self.nodes[j].key > key and key < min:
                min = self.nodes[j].key
        if min == float('inf'):
            print(0)
        else:
            print(min)

tree = binTree()
with open('input.txt') as f:
    while True:
        command = f.readline()
        if command == '':
            break
        command = list(map(str, command.split()))
        key = int(command[1])
        command = command[0]
        if command == '+':
            tree.insert(key)
        else:
            tree.findMinMore(key)