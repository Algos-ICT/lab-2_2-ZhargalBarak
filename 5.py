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

    def next(self, key):
        min = float('inf')
        for j in self.nodes:
            if self.nodes[j].key > key and key < min:
                min = self.nodes[j].key
        if min == float('inf'):
            print('none')
        else:
            print(min)

    def prev(self, key):
        max = float('-inf')
        for j in self.nodes:
            if self.nodes[j].key < key and key > max:
                max = self.nodes[j].key
        if max == float('-inf'):
            print('none')
        else:
            print(max)

    def nextNode(self, node):
        if not node.right:
            return node.right
        if not node.right.left:
            return node.right
        node = node.right
        while node.left:
            node = node.left
        return node

    def delete(self, key):
        if key in self.nodes:
            node = self.nodes[key]
            replace = self.nextNode(node)
            if not replace:
                if not node.parent:
                    if not node.left:
                        self.root = None
                    else:
                        node.left.parent = None
                        self.root = node.left
                else:
                    if not node.left:
                        if node.parent.left == node:
                            node.parent.left = None
                        else:
                            node.parent.right = None
                    else:
                        if node.parent.left == node:
                            node.parent.left = node.left
                        else:
                            node.parent.right = node.left
                        node.left.parent = node.parent
            elif replace == node.right:
                if not node.parent:
                    replace.parent = None
                    if node.left:
                        replace.left = node.left
                        node.left.parent = replace
                    self.root = replace
                else:
                    if node.parent.left == node:
                        node.parent.left = replace
                    else:
                        node.parent.right = replace
                    replace.parent = node.parent
                    if node.left:
                        replace.left = node.left
                        node.left.parent = replace
            else:
                if not node.parent:
                    if not node.left:
                        if not replace.right:
                            replace.parent.left = None
                        else:
                            replace.parent.left = replace.right
                            replace.right.parent = replace.parent
                        replace.right = node.right
                        node.right.parent = replace
                        replace.parent = None
                        self.root = replace
                    else:
                        if not replace.right:
                            replace.parent.left = None
                        else:
                            replace.parent.left = replace.right
                            replace.right.parent = replace.parent
                        replace.right = node.right
                        node.right.parent = replace
                        replace.left = node.left
                        node.left.parent = replace
                        replace.parent = None
                        self.root = replace
                else:
                    if not node.left:
                        if not replace.right:
                            replace.parent.left = None
                        else:
                            replace.parent.left = replace.right
                            replace.right.parent = replace.parent
                        replace.right = node.right
                        node.right.parent = replace
                        replace.parent = node.parent
                        if node.parent.left == node:
                            node.parent.left = replace
                        else:
                            node.parent.right = replace
                    else:
                        if not replace.right:
                            replace.parent.left = None
                        else:
                            replace.parent.left = replace.right
                            replace.right.parent = replace.parent
                        replace.right = node.right
                        node.right.parent = replace
                        replace.left = node.left
                        node.left.parent = replace
                        replace.parent = node.parent
            self.nodes.pop(key)


tree = binTree()
with open('input.txt') as f:
    while True:
        command = f.readline()
        if command == '':
            break
        command = list(map(str, command.split()))
        key = int(command[1])
        command = command[0]
        if command == 'insert':
            tree.insert(key)
        elif command == 'delete':
            tree.delete(key)
        elif command == 'exists':
            if key in tree.nodes:
                print('true')
            else:
                print('false')
        elif command == 'next':
            tree.next(key)
        elif command == 'prev':
            tree.prev(key)