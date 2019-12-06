# Lookup O(n)
# Enqueue O(1)
# Dequeue O(1)
# Peek O(1)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.length = 0

    def __str__(self):
        if self.front is None:
            return str(self.front)
        else:
            current_node = self.front
            output = ''
            while current_node is not None:
                output += str(current_node) + ' --> '
                current_node = current_node.next

            return output

    def peek(self):
        if self.front is None:
            return None
        return self.front.data

    def enqueue(self, value):
        node = Node(value)
        if self.front is None:
            self.front = node
            self.rear = node
        self.rear.next = node
        self.rear = node

        self.length += 1

    def dequeue(self):
        if self.front is None:
            return None
        if self.front == self.rear:
            self.front = self.rear = None
        self.front = self.front.next

        self.length -= 1

    def is_empty(self):
        return self.length == 0


# Tests
queue = Queue()
queue.enqueue('Google')
queue.enqueue('Udemy')
queue.enqueue('Discord')
print(queue)
print(queue.peek())
queue.dequeue()
print(queue)
