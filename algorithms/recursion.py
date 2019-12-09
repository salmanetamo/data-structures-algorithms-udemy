def find_factorial_recursive(number):
    if number < 2:
        return 1
    return number * find_factorial_recursive(number - 1)


def find_factorial_iterative(number):
    if number == 0:
        return 1
    result = 1
    while number > 0:
        result *= number
        number -= 1

    return result


def fibonacci_recursive(n):
    return n if n < 2 else fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iterative(n):
    fib_sequence = [0, 1]
    for i in range(2, n + 1):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])

    return fib_sequence[n]


# Tests factorial
print(find_factorial_recursive(4))
print(find_factorial_iterative(4))


# Tests fibonacci
print(fibonacci_recursive(0))
print(fibonacci_recursive(1))
print(fibonacci_recursive(5))
print(fibonacci_recursive(6))
print(fibonacci_iterative(0))
print(fibonacci_iterative(1))
print(fibonacci_iterative(5))
print(fibonacci_iterative(6))

