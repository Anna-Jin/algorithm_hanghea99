# 14장 트리 - 45. 이진 트리 반전 (Invert Binary Tree)

# 중앙을 기준으로 이진 트리를 반전시켜라.

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



def invertTree(root):
    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node:
            node.left, node.right = node.right, node.left

            queue.append(node.left)
            queue.append(node.right)

    return root

root = [4,2,7,1,3,6,9]

print(invertTree(make_tree_by(root, 0)))


