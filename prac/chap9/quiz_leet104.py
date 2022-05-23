# 14장 트리 - 42. 이진 트리의 최대 깊이 (Maximum Depth of Binary Tree)
# 이진 트리의 최대 깊이를 구하라

from collections import deque
from make_tree import make_tree_by

list = [3,9,20,None,None,15,7]


def max_depth(list):
    root = make_tree_by(list, 0)
    if not root:
        return 0

    q = deque([root])
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


print(max_depth(list))