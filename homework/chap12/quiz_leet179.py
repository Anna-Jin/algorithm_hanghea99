# 17장 정렬 - 61. 가장 큰 수 (Largest Num)
# 항목들을 조합하여 만들 수 있는 가장 큰 수를 출력하라.
from typing import List

nums = [3,30,34,5,9]


def largestNumber(nums: List[int]) -> str:
    for i in range(1, len(nums)):
        val = nums[i]
        cmp = i - 1

        while nums[cmp] > val and cmp >= 0:
            nums[cmp + 1] = nums[cmp]
            cmp -= 1

        nums[cmp + 1] = val
    return nums


print(largestNumber(nums))