n = int(input())
lines = [tuple(map(int, input().split())) for _ in range(n)]

checked = [0] * 101


for a, b in lines:
    print(a, b)
