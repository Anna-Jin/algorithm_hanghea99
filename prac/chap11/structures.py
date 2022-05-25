class BinaryMaxHeap:
    def __init__(self):
        # 계산 편의를 위해 0이 아닌 1번째 인덱스부터 사용한다.
        self.items = [None]

    def __len__(self):
        # 1번째 인덱스부터 사용하기 때문에 -1을 해준다.
        return len(self.items) - 1

    def _percolate_up(self):
        # 현재 인덱스를 가장 마지막 인덱스 지정
        cur = len(self)

        # 부모의 왼쪽 자식 노드는 2*cur, 오른쪽 자식 노드는 2*cur+1이므로 부모노드는 항상 cur//2이다.
        parent = cur // 2

        while parent > 0:
            # 현재 노드가 부모 노드보다 크다면 위치를 바꿔준다.
            if self.items[cur] > self.items[parent]:
                self.items[cur], self.items[parent] = self.items[parent], self.items[cur]

            # 다음 비교를 위해 현재 인덱스는 우리가 방금 비교한 부모 인덱스인 parent로, parent는 새롭게 비교할 부모 인덱스로 바꿔준다.
            cur = parent
            parent = cur // 2

    def _percolate_down(self, cur):
        biggest = cur
        left = 2 * cur
        right = 2 * cur + 1

        # 왼쪽 자식 노드와 비교한다.
        # 왼쪽 자식 노드의 인덱스가 (당연히) 마지막 노드가 아니고, 그 값이 현재의 biggest보다 크다면
        # biggest의 값을 left로 바꿔준다.
        if left <= len(self) and self.items[left] > self.items[biggest]:
            biggest = left

        # 오른쪽 자식 노드도 똑같이 비교한다.
        if right <= len(self) and self.items[right] > self.items[biggest]:
            biggest = right

        # biggest가 바뀌었다면 현재 노드와 바꿔준다.
        if biggest != cur:
            self.items[cur], self.items[biggest] = self.items[biggest], self.items[cur]
            # 재귀 호출로 계속 바꿔 준다. 마지막에는 최종적으로 가장 큰 값이 맨 아래로 내려가게 된다.
            self._percolate_down(biggest)

    def insert(self, k):
        # 힙 트리에 k값을 넣어준다. 가장 뒤에 들어가게 되므로 비교 연산 후 위치를 지정해준다.
        self.items.append(k)
        self._percolate_up()

    def extract(self):
        # 예외 처리. 힙이 비어있을 때 None을 리턴한다.
        if len(self) < 1:
            return None

        # __init__ 함수에서 가장 첫번째 인덱스를 1로 하기로 했으므로 루트 노드는 1번째 인덱스에 들어가게 된다.
        root = self.items[1]

        # 가장 첫번째 노드와 가장 마지막 노드를 바꿔준다. 힙에서 pop을 하면 가장 마지막 노드가 뽑혀나오기 때문.
        # 힙은 root노드만 pop 할 수 있다.
        self.items[1] = self.items[-1]

        # 맨 뒤로 옮겨준 root 노드를 추출한다
        self.items.pop()

        # 처음에 root노드와 바꾼 마지막 노드를 비교해서 적절한 위치에 배치해준다.
        self._percolate_down(1)

        # 어떻게 root노드를 pop했는데 다시 반환할 수 있죠?
        # 가장 처음에 우린 root 노드를 변수에 담아줬기 때문에 pop을 했더라도 이미 root 변수에 저장되어있다.
        return root