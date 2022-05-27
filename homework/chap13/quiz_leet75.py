# 75. Sort Colors

# 퀵 정렬
def quick_sort(lst, start, end):
    def partition(part, ps, pe):
        pivot = part[pe]
        i = ps - 1

        for j in range(ps, pe):
            if part[j] < pivot:
                i += 1
                part[i], part[j] = part[j], part[i]

        part[i + 1], part[pe] = part[pe], part[i + 1]

        return i + 1

    if start >= end:
        return None

    p = partition(lst, start, end)

    quick_sort(lst, start, p - 1)
    quick_sort(lst, p + 1, end)

    return lst


lst = [1, 4, 5, 3, 6]

print(quick_sort(lst, 0, len(lst) - 1))

