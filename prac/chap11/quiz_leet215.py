# (Kth Largest Element in an Array)
import heapq


def findKthLargest(nums, k):
    return heapq.nlargest(k, nums)

print(findKthLargest([3, 2, 1, 5, 6, 4], 2)[-1])