n, k = tuple(map(int, input().split()))
lst = [tuple(map(int, input().split())) for _ in range(k)]

box = [0] * (n + 1)

for a, b in lst:
    for i in range(a, b + 1):
        box[i] += 1


print(max(box))




