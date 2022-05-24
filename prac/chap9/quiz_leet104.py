# 14장 트리 - 42. 이진 트리의 최대 깊이 (Maximum Depth of Binary Tree)
# 이진 트리의 최대 깊이를 구하라
from collections import deque


class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right



def make_tree_by(list, index):
    parent = None

    if index < len(list):
        value = list[index]
        if value is None:
            return

        parent = TreeNode(value)
        parent.left = make_tree_by(list, 2 * index + 1)
        parent.right = make_tree_by(list, 2 * index + 2)

    return parent



def max_depth(list):

    q = deque([list])
    depth = 0

    while q:
        depth += 1
        for _ in range(len(q)):
            cur = q.popleft()
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

    return depth


list = [1,2,3,4,5,6,6,8,9]

print(max_depth(make_tree_by(list, 0)))