def group(lst, n):
    left = 0
    right = len(lst) - 1

    groups = []

    lst.sort()

    for _ in range(n):
        groups.append(sum((lst[left], lst[right])))
        left += 1
        right -= 1

    return max(groups)


lst = [3, 5, 5, 2]
n = 2

print(group(lst, n))