# n이 짝수면 2로 나누고, n이 홀수면 3을 곱하고 1을 더하는 것을 n이 1이 되기 전까지 계속 반복해야한다
# 몇 번을 반복해야 1이 되는지

n = int(input())

def recursive(n, cnt):
    if n < 2:
        print(cnt)
        return

    cnt += 1

    if n % 2 == 0:
        recursive(n // 2, cnt)
    else:
        recursive(n * 3 + 1, cnt)


recursive(n, 0)