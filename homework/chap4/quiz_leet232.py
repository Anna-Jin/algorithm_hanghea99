# 9장 스택, 큐 - 24 스택을 이용한 큐 구현 (Implement Queue using Stacks)
# 스택을 이용해 다음 연산을 지원하는 큐를 구현하라.

# push(x) - 요소 x를 큐 마지막에 삽입
# pop() - 큐 처음에 있는 요소를 제거
# peek() - 큐 처음에 있는 요소를 조회
# empty()- 큐가 비어있는지 여부를 리턴


# 내 풀이 - 파이참에서는 답이 제대로 나오는데 리트코드에 넣으면 다르게 나온다. 왜지?
class MyQueue:
    def __init__(self):
        self.q = []

    def push(self, item):
        self.q.append(item)

    def pop(self):
        if not self.q:
            return
        self.q.reverse()
        return self.q.pop()

    def peek(self):
        if not self.q:
            return
        return self.q[0]

    def empty(self):
        return len(self.q) == 0


# 해설 풀이 - 스택을 두개 사용하는 방식이다. 스택만의 연산을 사용하기 위해 이런 방식을 가져갔다고 한다.
class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x):
        self.input.append(x)

    def peek(self):
        # output이 없으면 모두 input에 넣어준다.
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())    # input에 값이 있는 동안 while문을 돌며 output에 먼저 들어간 순서대로 넣어준다. 이렇게 되면 pop을 했을 때, 가장 처음에 들어간 값이 꺼내진다.

        return self.output[-1] # 큐의 가장 위에 있는 요소를 보여준다.

    def pop(self):
        self.peek() # 선입선출을 하기 위해 peek로 pop을 했을 때 가장 먼저 들어간 요소가 꺼내기게 정렬한다.
        return self.output.pop()

    def empty(self):
        return self.input == [] and self.output == []

queue = MyQueue()

queue.push(1)
queue.push(2)
queue.push(3)
queue.push(4)
print(queue.pop())
queue.push(5)
print(queue.pop())
print(queue.pop())
print(queue.pop())
print(queue.pop())