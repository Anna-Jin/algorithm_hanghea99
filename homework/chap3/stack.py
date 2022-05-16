class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, val):
        self.top = Node(val, self.top)

    def pop(self):
        if not self.top:
            return None

        node = self.top.item
        self.top = self.top.next

        return node
