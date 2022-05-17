import collections


class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next


class Queue:
    def __init__(self):
        self.front = None

    def is_empty(self):
        return self.front is None

    def push(self, value):
        if not self.front:
            self.front = Node(value, None)

        node = self.front
        while node.next:
            node = node.next

        node.next = Node(value, None)

    def pop(self):
        if not self.front:
            return None

        node = self.front
        self.front = self.front.next
        return node.item