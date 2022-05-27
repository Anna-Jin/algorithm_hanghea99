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

# 리스트를 정렬 후 합쳐주기 위한 함수
def merge(arr1, arr2):
    # 결과를 담아줄 빈 배열
    result = []

    # 하나씩 선택할 포인터
    i = j = 0

    # 각각 비교 후 result에 담아준다
    while i < len (arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    # 비교가 끝나고 남은 요소들 result에 삽입
    while i < len(arr1):
        result.append(arr1[i])
        i += 1

    while j < len(arr2):
        result.append(arr2[j])
        j += 1

    return result


def merge_sort(lst):
    # 예외 처리
    if len(lst) <= 1:
        return lst

    # 재귀를 이용하여 리스트를 끝까지 쪼개준다.
    mid = len(lst) // 2
    L = merge_sort(lst[:mid])
    R = merge_sort(lst[mid:])

    return merge(L, R)


assert merge_sort([4, 6, 2, 9, 1]) == [1, 2, 4, 6, 9]