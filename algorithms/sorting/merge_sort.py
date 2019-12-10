def merge_sort(array):
    '''
    Time complexity: O(n * log(n))
    Space complexity: O(n)
    :param array:
    :return: array
    '''

    def merge(left, right):
        result = []
        left_index, right_index = 0, 0
        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                result.append(left[left_index])
                left_index += 1
            else:
                result.append(right[right_index])
                right_index += 1
        result.extend(left[left_index:])
        result.extend(right[right_index:])
        return result

    if len(array) == 1:
        return array

    array_left = array[:len(array)//2]
    array_right = array[len(array)//2:]
    return merge(merge_sort(array_left), merge_sort(array_right))


# Tests
array = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
print(merge_sort(array))
