n, k, t = tuple(input().split())

lst = [input() for _ in range(int(n))]

result = []

for word in lst:
    if word.startswith(t):
        result.append(word)



print(result)