n = int(input())

def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)

print(factorial(n))


# 실수한 부분
# return 부분을 재귀 호출로 안하고 그냥 곱해버림........