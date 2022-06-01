def sequence(n):
    # 종료 조건
    if n == 1:
        return 2
    if n == 2:
        return 4

    return sequence(n - 1) * sequence(n - 2) % 100


print(sequence(4))


