# Maximum Product of Two Elements in an Array
import heapq


def maxProduct(nums):
    if len(nums) == 2:
        return (nums[0] - 1) * (nums[1] - 1)

    heap = []

    # 최대 힙으로 바꾸는 거 (튜플로)
    for num in nums:
        heapq.heappush(heap, (-num, num))

    # 인덱스 기준으로 정렬
    heap.sort()

    # 뽑아보려고 한거
    i = heapq.heappop(heap)
    j = heapq.heappop(heap)

    return (i[1] - 1) * (j[1] - 1)


nums = [3,4,5,2]

print(maxProduct(nums))