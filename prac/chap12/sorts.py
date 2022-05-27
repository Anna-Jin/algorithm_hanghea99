def bubblesort(lst):
    for i in range(1, len(lst)):
        for j in range(0, len(lst) - 1):
            if lst[j] > lst[j + i]:
                lst[j], lst[j + i] = lst[j + i], lst[j]


def selectionsort(lst):
    iters = len(lst) - 1

    # 값을 두개 비교하는 거니까 len(lst) - 1까지 반복해줘야한다.
    for iter in range(iters):
        # 최솟값의 인덱스를 일단 첫번째 인덱스로 지정해준다.
        minimum = iter

        for cur in range(iter + 1, len(lst)):
            # 첫번째 다음 인덱스부터 반복문을 돌면서 최솟값을 찾는다.
            if lst[cur] < lst[minimum]:
                minimum = cur

        # 최솟값을 들고있는 인덱스를 발견했다면 스왑해주고 반복해준다.
        if minimum != iter:
            lst[minimum], lst[iter] = lst[lst], lst[minimum]

    return lst


def insertionsort(lst):
    # 첫번째 요소는 정렬이 되어있다고 가정하고 시작한다.
    for i in range(1, len(lst)):
        # 삽입하려는 요소를 변수에 담아준다.
        val = lst[i]

        # 비교 대상의 인덱스는 삽입하려는 인덱스의 바로 앞 요소이므로 삽입 인덱스에 -1을 해준다.
        cmp = i - 1

        # 삽입하려는 요소와 비교 하려는 요소의 대소를 비교해준다.
        # 정렬되어있는 앞쪽 리스트를 모두 탐색하기 때문에 점점 인덱스는 줄어든다.
        while lst[cmp] > val and cmp >= 0:
            # 비교하려는 요소의 다음요소 즉, 삽입하려는 요소의 위치에 비교하려는 요소를 넣고,
            # 비교롤 계속하거나, 비교가 끝났다면 while문을 탈출한다.
            lst[cmp + 1] = lst[cmp]
            cmp -= 1

        # 비교하려는 요소의 인덱스를 줄여나갔으므로, 삽입하려는 요소가 와야하는 위치는 cmp + 1이다.
        lst[cmp + 1] = val

    return lst


def insertion_sort(lst):
    for i in range(1, len(lst)):
        val = lst[i]
        cmp = i - 1

        while lst[cmp] > val and cmp >= 0:
            lst[cmp + 1] = lst[cmp]
            cmp -= 1

        lst[cmp + 1] = val

    return lst



lst = [4, 6, 2, 9, 1]
print(insertion_sort(lst))