# 18장 이진 검색 - 65. 이진 검색 (Binary Search)

# 직접 구현
# 타겟의 위치(인덱스)를 알려준다
def binary_search(nums, target):
    def bs(start, end):
        if start > end:
            return -1

        mid = (start + end) // 2

        if nums[mid] < target:
            return bs(mid + 1, end)
        elif nums[mid] > target:
            return bs(start, mid - 1)
        else:
            return mid

    return bs(0, len(nums) - 1)


# 내장 모듈 이용
import bisect

def binary_search_builtin(nums, target):
    idx = bisect.bisect_left(nums, target)

    if idx < len(nums) and nums[idx] == target:
        return idx
    else:
        return -1


print(binary_search_builtin([1,2,3,4,5,6,7,8,5,4,3], 4))


# 반복풀이
def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2

        # 찾으려는 값이 중간값보다 클 때, 다음 찾을 범위는 중간값 다음부터 마지막까지
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid
    return -1