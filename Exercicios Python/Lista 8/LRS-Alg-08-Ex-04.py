def fibonacci_memo(n, memo=None):
    if memo is None:
        memo = {}

    if n == 0:
        return 0
    elif n == 1:
        return 1
    if n in memo:
        return memo[n]

    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

def main():
    test_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 40, 50]
    for value in test_values:
        print(f"Fibonacci({value}) = {fibonacci_memo(value)}")

if __name__ == "__main__":
    main()