class Array:
    def __init__(self):
        self.length = 0
        self.data = []

    def __str__(self):
        return str(self.data)

    def get(self, index):
        return self.data[index]

    def push(self, item):
        self.data.append(item)
        self.length += 1
        return self.length

    def pop(self):
        last_item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1

        return last_item

    def delete(self, index):
        item = self.data[index]
        self.shift_items(index)

        return item

    def shift_items(self, index):
        for i in range(index, self.length):
            self.data[i] = self.data[i + 1]

        del self.data[self.length - 1]
        self.length -= 1


# Test examples
array = Array()
array.push('Hi')
array.push('I')
array.push('am')


# Example exercises
def reverse1(string):
    '''
    Extra memory
    Time complexity: O(n)
    Space complexity: O(n)
    '''
    new_string = ''
    for char in string:
        new_string += char

    return char


def merge_sorted_arrays(array1, array2):
    merged_array = []
    array1_index = 0
    array2_index = 0

    while len(merged_array) < len(array1) + len(array2):
        item = None
        if array1_index < len(array1):
            if array2_index < len(array2):
                if array1[array1_index] >= array2[array2_index]:
                    item = array2[array2_index]
                    array2_index += 1
                else:
                    item = array1[array1_index]
                    array1_index += 1
            else:
                item = array1[array1_index]
                array2_index += 1
        else:
            if array2_index < len(array2):
                item = array2[array2_index]

        merged_array.append(item)
    return merged_array


print(merge_sorted_arrays([0, 3, 4, 31], [4, 6, 30]))

# print(reverse1('Salmane'))
# print(reverse2('Salmane'))
# Intro
# strings = ['a', 'b', 'c', 'd']
#
# strings.append('e')  # O(1) Push at the end of array
# print(strings)
#
# strings.pop()  # O(1) Pop end of array
# print(strings)
#
# strings.insert(0, 'x')  # O(n) Insert at given index
# print(strings)
#
# strings.remove('c')  # O(n) Delete at given index
# print(strings)
