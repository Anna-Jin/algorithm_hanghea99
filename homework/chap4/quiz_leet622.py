# 9장 스택, 큐 - 25. 원형 큐 디자인 (Design Circular Queue)
# 원형 큐 디자인하라.

# 원형 큐?
# 마지막 위치가 시작 위치와 연결되는 원형 구조를 띠기 때문에, 링 버퍼(Ring Buffer)라고도 부른다.

# 배열로 구현하기

class MyCircularQueue:
    def __init__(self, k: int):
        self.q = [None] * k # 공간 설정
        self.maxlen = k # 최대 길이
        self.front = 0
        self.rear = 0

    # rear 포인터 이동
    def enQueue(self, value: int) -> bool:
        # rear 포인터의 위치에 값이 없다면 추가해준다.
        if self.q[self.rear] is None:
            self.q[self.rear] = value
            # rear가 다음 포인터로 이동해준다 (self.rear), 만약 rear가 전체길이를 초과하면 % 모듈로 나머지를 계산해 넣어준다. 그러면 결국 rear는 맨 앞으로 돌아오게 된다.
            # ex) maxlen = 3, rear = 2 -> rear = (2 + 1) % 3 = 0
            self.rear = (self.rear + 1) % self.maxlen
            return True
        else:
            # rear포인터 위치가 None이 아니면 (앞으로 한칸 이동 시켰기 때문에 요소가 가득 차지 않았다면 None이어야한다.), 비정상적인 상태이므로 False를 리턴한다.
            return False

    # front 포인터 이동
    def deQueue(self) -> bool:
        # front 포인터 위치에 값이 없을 때는 삭제할 요소가 없으므로 False 리턴
        if self.q[self.front] is None:
            return False
        else:
            self.q[self.front] = None # front가 가리키는 요소를 삭제해준다.
            self.front = (self.front + 1) % self.maxlen
            return True

    def Front(self) -> int:
        # front에 요소가 들어있지 않으면 -1 리턴, 아니면 front 요소 리턴
        if self.q[self.front] is None:
            return -1
        else:
            return self.q[self.front]

    def Rear(self) -> int:
        # rear는 맨 끝의 다음 요소를 가리키고 있기 때문에, 그 값을 가져오려면 -1을 해줘야한다.
        if self.q[self.rear - 1] is None:
            return -1
        else:
            return self.q[self.rear - 1]

    def isEmpty(self) -> bool:
        # rear와 front가 같다는 건 원형 큐가 비어있다는 말이다. 또, front는 제일 앞의 값을 가리키고 있는데 이 값이 None이라면 이 원형 큐는 비어있는게 된다.
        return self.front == self.rear and self.q[self.front] is None

    def isFull(self) -> bool:
        # isEmpty와 비슷하지만 차이점은 front가 가리키는 요소에 값이 들어있을 때 True를 반환한다.
        return self.front == self.rear and self.q[self.front] is not None