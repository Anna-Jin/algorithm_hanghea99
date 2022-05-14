class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    # 리스트 삽입
    def append(self, val):
        # 리스트가 비어있을 때 즉, head가 비어있을 때는 head를 지정해주고 끝낸다.
        if not self.head:
            self.head = ListNode(val, None)
            return

        # 현재 바라보고 있는 node를 head로 지정해준다.
        node = self.head

        # node를 제일 끝으로 옮겨준다.
        while node.next:    # node에 next(화살표)가 있는 동안 반복 -> 맨 끝으로 이동한다.
            node = node.next
        node.next = ListNode(val, None)


# list를 linkedList로 바꿔보자!
list = [1, 2, 3]

l1 = LinkedList()

for e in list:
    l1.append(e)
print(l1)
