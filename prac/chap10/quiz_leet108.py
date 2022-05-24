# 14장 트리 - 50. 정렬된 배열의 이진 탐색 트리 변환
# 오름차순으로 정렬된 배열을 눂이 균형 이진 탐색 트리로 변환하라


nums = [-10, -3, 0, 5, 9]


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sortedArrayToBST(nums):
    if not nums:
        return None

    # 주어진 배열을 반으로 쪼개준다. // 연산자는 나눈 몫의 정수만 남겨준다.
    mid = len(nums) // 2

    node = TreeNode(nums[mid])
    node.left = sortedArrayToBST(nums[:mid])
    node.right = sortedArrayToBST(nums[mid + 1:])

    return node
