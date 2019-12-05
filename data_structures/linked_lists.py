# Prepend O(1)
# Append O(1)
# Lookup O(n)
# Delete O(n)
# Insert O(n)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = self.head
        self.length = 0

    def __str__(self):
        if self.head is None:
            return str(self.head)
        else:
            current_node = self.head
            output = ''
            while current_node is not None:
                output += str(current_node) + ' --> '
                current_node = current_node.next

            return output

    def append(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail = node

        self.length += 1

    def prepend(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            node.next = self.head
            self.head = node
        self.length += 1

    def get(self, index):
        if self.head is None:
            return None
        else:
            current_node = self.head
            counter = 0
            while current_node is not None:
                if counter == index:
                    return current_node.data
                current_node = current_node.next
                counter += 1

            return None

    def insert(self, index, value):
        if index >= self.length:
            return False

        node = Node(value)
        if self.head is None:
            if index != 0:
                return False
            else:
                self.head = node
                self.tail = self.head
        else:
            current_node = self.head
            counter = 0
            while current_node is not None:
                if counter + 1 == index:
                    node.next = current_node.next
                    current_node.next = node
                    if index + 1 == self.length:
                        self.tail = node

                    break
                current_node = current_node.next
                counter += 1
        self.length += 1
        return True

    def delete(self, index):
        if index >= self.length:
            return False

        if self.head is None:
            return False
        else:
            current_node = self.head
            counter = 0
            while current_node is not None:
                if counter + 1 == index:
                    current_node.next = current_node.next.next
                    if index + 1 == self.length:
                        self.tail = current_node.next

                    break
                current_node = current_node.next
                counter += 1
        self.length -= 1
        return True

    def reverse(self):
        if self.head is None:
            return False
        else:
            current_node = self.head
            next_node = current_node.next
            self.tail = self.head
            while next_node is not None:
                temp = next_node.next
                next_node.next = current_node
                current_node = next_node
                next_node = temp
            self.head.next = None
            self.head = current_node
        return True


# Tests
linked_list = LinkedList()
linked_list.append(1)
linked_list.append(3)
linked_list.prepend(0)
linked_list.prepend(-1)
print(linked_list.insert(3, 2))
print(linked_list.delete(1))
print(linked_list.reverse())
print(linked_list)
# print(linked_list.get(1))
