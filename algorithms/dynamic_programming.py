def fibonacci_memoized(n, memo):
    if n in memo:
        return memo[n]
    else:
        if n < 2:
            return n
        memo[n] = fibonacci_memoized(n - 1, memo) + fibonacci_memoized(n - 2, memo)
        return memo[n]


# Tests
print(fibonacci_memoized(0, {}))
print(fibonacci_memoized(1, {}))
print(fibonacci_memoized(5, {}))
print(fibonacci_memoized(6, {}))
