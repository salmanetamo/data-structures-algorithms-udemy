# Know data structures and algorithms

a1 = ['a', 'b', 'c', 'x''a', 'b', 'c','a', 'b', 'c','a', 'b', 'c','a', 'b', 'c','a', 'b', 'c','a', 'b', 'c','a', 'b', 'c','a', 'b', 'c','a', 'b', 'c','a', 'b', 'c','a', 'b', 'c','a', 'b', 'c','a', 'b', 'c','a', 'b', 'c','a', 'b', 'c','a', 'b', 'c','a', 'b', 'c','a', 'b', 'c']
a2 = ['z', 'y', 'i''z', 'y','z', 'y','z', 'y','z', 'y','z', 'y','z', 'y','z', 'y','z', 'y','z', 'y','z', 'y','z', 'y']
a3 = ['z', 'y', 'x']
# Quadratic
def find_common_quadratic(array1, array2):
    for element_array1 in array1:
        for element_array2 in array2:
            if element_array1 == element_array2:
                return True
    return False

# Linear
def find_common_linear(array1, array2):
    array_set = set(array1)
    for element in array2:
        if element in array_set:
            return True
    return False

print(find_common_quadratic(a1, a3))

import timeit

import timeit

start1 = timeit.timeit()
print(find_common_quadratic(a1, a2))
end1 = timeit.timeit()
print(end1 - start1)

start2 = timeit.timeit()
print(find_common_linear(a1, a2))
end2 = timeit.timeit()
print(end2 - start2)