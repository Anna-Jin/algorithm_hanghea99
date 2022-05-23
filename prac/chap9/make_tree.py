from structure import TreeNode


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
