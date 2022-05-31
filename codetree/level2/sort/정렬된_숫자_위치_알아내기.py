n = int(input())

lst = []

for i, num in enumerate(list(map(int, input().split()))):
    lst.append((i, num))

sorted_lst = sorted(lst, key=lambda x : x[1])

result = []

for a in lst:
    result.append(sorted_lst.index(a) + 1)

print(' '.join(map(str, result)))

