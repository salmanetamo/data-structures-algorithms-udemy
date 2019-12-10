def bubble_sort(array):
    '''
    Time complexity: O(n^2)
    Space complexity: O(1)
    :param array:
    :return: array
    '''
    for i in range(len(array)):
        for j in range(len(array)):
            try:
                if array[j] > array[j + 1]:
                    temp = array[j]
                    array[j] = array[j + 1]
                    array[j + 1] = temp
            except IndexError:
                continue
    return array


# Tests
array = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(bubble_sort(array))