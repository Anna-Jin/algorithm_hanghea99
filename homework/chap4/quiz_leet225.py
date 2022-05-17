# 9장 스택, 큐 - 23. 큐를 이용한 스택 구현
# 큐를 이용해 다음 연산을 지원하는 스택을 구현하라

# push(x) - 요소 x를 스택에 삽입
# pop() - 스택의 첫 번째 요소 삭제
# top() - 스택의 첫 번째 요소 가져오기
# empty() - 스택이 비어있는 지 판별
import collections


class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next


class MyStack:
    def __init__(self):
        # 큐를 데크로 선언
        self.q = collections.deque()

    def push(self, x):
        self.q.append(x)
        for _ in range(len(self.q) - 1): # 맨 뒤에 삽입한 요소의 앞까지 반복문 돌림
            self.q.append(self.q.popleft()) # 맨 앞의 요소를 꺼내서 맨 뒤로 옮겨준다. 이러면 맨 뒤에 append한 요소가 맨 앞으로 간다.

    def pop(self):
        if not self.q:
            return
        return self.q.popleft()

    def top(self):
        if not self.q:
            return
        return self.q[0]

    def empty(self):
        return len(self.q) == 0


stack = MyStack()

stack.push(1)
stack.push(2)
print(stack.top())
print(stack.pop())
print(stack.empty())