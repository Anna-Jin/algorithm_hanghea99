def sequence(n):
    # n이 1이 되기 전까지 반복한다.
    if n == 1:
        return 0

    if n % 2 == 0:
        return sequence(n / 2) + 1
    else:
        return sequence(n * 3 + 1) + 1


print(sequence(3))

