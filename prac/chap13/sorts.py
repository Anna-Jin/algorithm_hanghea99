def quick_sort(lst, start, end):
    def partition(part, ps, pe):
        # 기준점을 가장 오른쪽 요소로 잡는다.
        pivot = part[pe]

        # pivot보다 작은 집합의 인덱스 i를 -1로 잡아둔다.
        i = ps - 1

        # 정렬하려는 집합의 범위 [ps:pe]
        for j in range(ps, pe):

            # pivot보다 작은 값을 발견했다면 왼쪽 집합으로 나열해줘야햐므로
            # i 인덱스의 요소와 현재 가리키고 있는 j 인덱스의 요소를 바꿔준다.
            if part[j] <= pivot:
                i += 1
                part[i], part[j] = part[j], part[i]

        # pivot보다 더 큰 값이 되는 부분인 i + 1과 pivot의 요소를 바꿔준다.
        part[i + 1], part[pe] = part[pe], part[i + 1]
        return i + 1

    # 재귀 종료 조건
    if start >= end:
        return None

    p = partition(lst, start, end)
    # pivot의 왼쪽 집합 재귀
    quick_sort(lst, start, p - 1)

    # pivot의 오른쪽 집합 재귀
    quick_sort(lst, p + 1, end)

    return lst


lst = [1, 4, 3, 2, 9, 5]

assert quick_sort([1, 4, 3, 2, 9, 5], 0, 5) == [1, 2, 3, 4, 5, 9]