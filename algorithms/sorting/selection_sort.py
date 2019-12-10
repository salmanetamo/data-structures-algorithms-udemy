def selection_sort(array):
    '''
    Time complexity: O(n^2)
    Space complexity: O(1)
    :param array:
    :return: array
    '''

    for i in range(len(array)):
        current = array[i]
        min_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        array[i] = array[min_index]
        array[min_index] = current
    return array


# Tests
array = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(selection_sort(array))
