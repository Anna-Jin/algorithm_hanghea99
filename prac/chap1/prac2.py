# Q. 다음과 같은 숫자로 이루어진 배열이 있을 때, 이 배열 내에 특정 숫자가 존재한다면 True, 존재하지 않다면 False 를 반환하시오.

arr = [3, 5, 6, 1, 2, 4]


# 내 풀이
def is_num_exist(num, arr):
    if num in arr:
        return True
    else:
        return False


print(is_num_exist(3, arr))


# 강의 풀이
def is_number_exist(num, arr):
    for el in arr:
        if num == el:
            return True
    return False


print(is_number_exist(5, arr))  # O(N)


# 알고리즘의 성능은 입력값에 따라 달라질 수 있다.
# ex) 배열을 돌렸을 때, 찾는 값이 3이면 1번만에 값을 찾지만 찾는 값이 4면 그 이상이 걸린다.