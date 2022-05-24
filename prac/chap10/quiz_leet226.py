# 14장 트리 - 45. 이진 트리 반전 (Invert Binary Tree)

# 중앙을 기준으로 이진 트리를 반전시켜라.
import collections


def invertTree(root):
    queue = collections.deque([root])

    while queue:
        node = queue.popleft()
        if node:
            node.left, node.right = node.right, node.left

            queue.append(node.left)
            queue.append(node.right)

    return root


