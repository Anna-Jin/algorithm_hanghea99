# 교재
# class Node:
#     def __init__(self, item, next):
#         self.item = item
#         self.next = next
#
# class Stack:
#     def __init__(self):
#         self.last = None
#
#     def push(self, item):
#         self.last = Node(item, self.last)
#
#     def pop(self):
#         item = self.last.item # pop은 가장 마지막 item을 return해준다.
#         self.last = self.last.next
#         return item


# 강의
class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        self.top = Node(value, self.top)  # 지금의 top을 새로운 top으로 바꿔준다.

    def pop(self):
        if self.top is None:
            return None

        node = self.top.item
        self.top = self.top.next  # 여기서 next는 스택에서 가장 위인 top노드의 바로 아래 노드이다.

        return node

    def is_empty(self):
        return self.top is None


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)

for _ in range(5):
    print(stack.pop())
