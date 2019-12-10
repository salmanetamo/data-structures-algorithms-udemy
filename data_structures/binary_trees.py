class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

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

    def breadth_first_search(self):
        current_node = self.root
        result = []
        queue = list()

        queue.append(current_node)
        while len(queue) > 0:
            current_node = queue.pop(0)
            result.append(current_node)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)

        return result

    def breadth_first_search_recursive(self, queue, result):
        if len(queue) == 0:
            return result

        current_node = queue.pop(0)
        result.append(current_node)
        if current_node.left is not None:
            queue.append(current_node.left)
        if current_node.right is not None:
            queue.append(current_node.right)

        return self.breadth_first_search_recursive(queue, result)

    def dfs_in_order(self):
        def in_order(node, result):
            if node.left is not None:
                in_order(node.left, result)
            result.append(node)
            if node.right is not None:
                in_order(node.right, result)
            return result

        return in_order(self.root, [])

    def dfs_pre_order(self):
        def pre_order(node, result):
            result.append(node)
            if node.left is not None:
                pre_order(node.left, result)
            if node.right is not None:
                pre_order(node.right, result)
            return result

        return pre_order(self.root, [])

    def dfs_post_order(self):
        def post_order(node, result):
            if node.left is not None:
                post_order(node.left, result)
            if node.right is not None:
                post_order(node.right, result)
            result.append(node)
            return result

        return post_order(self.root, [])




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
# print(bst.lookup(170))
# traverse(bst.root)
# for node in bst.breadth_first_search():
#     print(node)
# for node in bst.breadth_first_search_recursive([bst.root], []):
#     print(node)

# for node in bst.dfs_in_order():
#     print(node)

# for node in bst.dfs_pre_order():
#     print(node)

for node in bst.dfs_post_order():
    print(node)
