class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.data < other.data

    def __gt__(self, other):
            return self.data > other.data

    def __eq__(self, other):
                return self.data == other.data


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
        else:
            current_node = self.root
            while True:
                if node < current_node:
                    if current_node.left is None:
                        current_node.left = node
                        break
                    else:
                        current_node = current_node.left
                elif node > current_node:
                    if current_node.right is None:
                        current_node.right = node
                        break
                    else:
                        current_node = current_node.right

    def lookup(self, value):
        if self.root is None:
            return False
        node = Node(value)
        current_node = self.root
        while current_node is not None:
            if node == current_node:
                return True
            elif node < current_node:
                if current_node.left is None:
                    return False
                else:
                    current_node = current_node.left
            elif node > current_node:
                if current_node.right is None:
                    return False
                else:
                    current_node = current_node.right



def traverse(node):
    '''
    In order traversal
    '''
    if node is None:
        print('Empty')

    if node.left is not None:
        traverse(node.left)
    print(node.data)
    if node.right is not None:
        traverse(node.right)

bst = BinarySearchTree()
bst.insert(9)
bst.insert(4)
bst.insert(6)
bst.insert(20)
bst.insert(170)
bst.insert(15)
bst.insert(1)
print(bst.lookup(170))
# traverse(bst.root)