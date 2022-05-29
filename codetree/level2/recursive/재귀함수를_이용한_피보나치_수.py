def fibonacci(n):
    if n <= 2:
        return 1

    fibo1 = fibonacci(n - 1)
    fibo2 = fibonacci(n - 2)

    return fibo1 + fibo2

print(fibonacci(4))