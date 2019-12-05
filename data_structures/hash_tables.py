# Search O(1)
# Lookup O(1)
# Delete O(1)
# Insert O(1)


class HashTable:
    def __init__(self, size):
        self.size = size
        self.data = [[] for i in range(size)]

    def __hash__(self, key):
        hashed_key = 0
        for i in range(len(key)):
            hashed_key = (hashed_key + ord(key[i]) * i) % self.size

        return hashed_key

    def set(self, key, value):
        address = self.__hash__(key)
        if not self.data[address]:
            self.data[address] = []
        self.data[address].append([key, value])

    def get(self, key):
        address = self.__hash__(key)
        current_bucket = self.data[address]
        if not current_bucket:
            for pair in current_bucket:
                if self.__hash__(pair[0]) == address:
                    return pair[1]

        return None

    def keys(self):
        keys = []
        for bucket in self.data:
            if not bucket:
                for pair in bucket:
                    keys.append(pair[0])

        return keys


# Tests
hash_table = HashTable(50)
hash_table.set('grapes', 100000)
hash_table.set('apples', 500)
# print(hash_table.get('apples'))
# print(hash_table.keys())


# Example interview question
# Find first recurring number
def first_recurring_number(array):
    '''
    Google Interview question.
    Time complexity: O(n)
    Space complexity: O(n)
    :param array:
    :return: first occurring number
    '''
    frequencies = dict()

    for number in array:
        if frequencies.get(number, -1) + 1 > 0:
            return number
        else:
            frequencies[number] = 1

    return None


def first_recurring_number2(array):
    '''
    Google Interview question.
    Time complexity: O(n ^ 2)
    Space complexity: O(1)
    :param array:
    :return: first occurring number
    '''

    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] == array[j]:
                return array[i]
    return None


print(first_recurring_number([2, 5, 1, 2, 3, 5, 1, 2, 4]))
print(first_recurring_number([2, 1, 1, 2, 3, 5, 1, 2, 4]))
print(first_recurring_number([2, 3, 5, 4]))

print(first_recurring_number2([2, 5, 1, 2, 3, 5,1, 2, 4]))
print(first_recurring_number2([2, 1, 1, 2, 3, 5, 1, 2, 4]))
print(first_recurring_number2([2, 3, 5, 4]))
