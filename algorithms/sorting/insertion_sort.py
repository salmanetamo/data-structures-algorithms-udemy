def insertion_sort(array):
    '''
    Good for small input, easy implementation

    Time complexity: O(n^2)
    Space complexity: O(1)
    :param array:
    :return: array
    '''

    for index in range(1, len(array)):
        value = array[index]
        i = index - 1
        while i >= 0:
            if value < array[i]:
                array[i + 1] = array[i]
                array[i] = value
                i -= 1
            else:
                break
    return array


# Tests
array = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(insertion_sort(array))
