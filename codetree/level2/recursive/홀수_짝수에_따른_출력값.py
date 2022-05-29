def print_sum(n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    return print_sum(n - 2) + n

print(print_sum(5))