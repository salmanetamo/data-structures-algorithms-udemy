# Lookup O(n)
# Pop O(1)
# Push O(1)
# Peek O(1)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = self.top
        self.length = 0

    def __str__(self):
        if self.top is None:
            return str(self.top)
        else:
            current_node = self.top
            output = ''
            while current_node is not None:
                output += str(current_node) + ' --> '
                current_node = current_node.next

            return output

    def peek(self):
        if self.top is None:
            return None
        return self.top.data

    def push(self, value):
        node = Node(value)
        if self.top is None:
            self.top = node
            self.bottom = self.top
        else:
            node.next = self.top
            self.top = node

        self.length += 1

    def pop(self):
        if self.top is None:
            return None
        if self.top == self.bottom:
            self.bottom = None
        node = self.top
        self.top = node.next

        self.length -= 1
        return node.data

    def is_empty(self):
        return self.length == 0


class StackArray:
    def __init__(self):
        self.array = []

    def __str__(self):
        output = ''
        for node in self.array[::-1]:
            output += str(node) + ' -- '
        return output

    def peek(self):
        if not self.array:
            return None
        return self.array[len(self.array) - 1].data

    def push(self, value):
        self.array.append(Node(value))

    def pop(self):
        self.array.pop()

    def is_empty(self):
        return len(self.array) == 0



# Tests
stack = StackArray()
stack.push('Google')
stack.push('Udemy')
stack.push('Discord')
print(stack)
print(stack.peek())
stack.pop()
print(stack)
