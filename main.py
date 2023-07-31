import timeit
import sys


def main():
    x = 500

    # Measure runtime and data usage for iterative Fibonacci function
    print("Iterative Fibonacci number for integer input:", x)
    start_time_iter = timeit.default_timer()
    result_iterative = fibonacci1(x)
    end_time_iter = timeit.default_timer()
    print("Result:", result_iterative)
    print("Runtime (iterative):", (end_time_iter - start_time_iter) * 1e6, "microseconds")
    print("Data usage (iterative):", sys.getsizeof(result_iterative), "bytes")

    print()

    # Measure runtime and data usage for optimized recursive Fibonacci function
    print("Optimized recursive Fibonacci number for integer input:", x)
    start_time_optimized = timeit.default_timer()
    result_recursive = fibonacci2(x)
    end_time_optimized = timeit.default_timer()
    print("Result:", result_recursive)
    print("Runtime (optimized recursive):", (end_time_optimized - start_time_optimized) * 1e6, "microseconds")
    print("Data usage (optimized recursive):", sys.getsizeof(result_recursive), "bytes")


def fibonacci1(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c
        return b


def fibonacci2(n, memo={}):
    if n < 0:
        print("Incorrect input")
        return None
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    elif n in memo:
        return memo[n]
    else:
        memo[n] = fibonacci2(n - 1, memo) + fibonacci2(n - 2, memo)
        return memo[n]


main()
