# O(1): Constant time
# O(log(n)): Logarithmic time
# O(n * log(n)): Log-linear time
# O(n): Linear time
# O(n^2): Quadratic time
# O(2^n): Exponential time
# O(n!): Factorial time

# Calculating Big-O
# Rule 1: Worst Case (We always only care about the worst case scenario)
# Rule 2: Remove constants (Drop all the constants after computing number of steps)
# Rule 3: Different terms for input (O(a + b) or O(a * b) for different sized inputs)
# Rule 4: Drop all dominants(Only choose the most dominant term)


# What causes space complexity
# Variables
# Data structures
# Function calls
# Allocations

import timeit


def find_nemo(array):
    start = timeit.timeit()
    for name in array:
        if name == 'nemo':
            print('Found nemo')
    end = timeit.timeit()
    print('It took: ' + str(end - start) + ' milliseconds')


find_nemo(['nemo'])