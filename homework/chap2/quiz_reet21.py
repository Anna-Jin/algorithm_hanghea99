# 8장 연결리스트 - 14. 두 정렬 리스트의 병합
# 정렬되어 있는 두 연결 리스트를 합쳐라

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        # 리스트가 비어있다면
        if not self.head:
            self.head = ListNode(val, None)  # head에 첫번째 값을 넣는다. 연결할 다음 노드는 없다.
        return

        # 비어있지 않는다면
        # 현재 바라보고 있는 노드를 head로 지정해준다.
        node = self.head

        # 마지막 노드(tail)로 이동해준다
        while node.next:
            node = node.next
        node.next = ListNode(val, None)


l1 = LinkedList()

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = LinkedList()
l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

# 내 접근 - 속도가 더 빠름
# 두 리스트의 데이터를 하나씩 꺼내서 배열에 담아 정렬한 다음 새로운 리스트에 담는다.
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    # 정렬하기 위한 배열
    l = []

    # 데이터 배열에 담기
    while l1:
        l.append(l1.val)
        l1 = l1.next
    while l2:
        l.append(l2.val)
        l2 = l2.next

    temp = None
    head = None  # 새로 만든 리스트

    for val in sorted(l):
        # temp 없을 때(빈 리스트), 새로운 node를 생성하고 result에 담는다.
        if not temp:
            temp = ListNode(val)
            head = temp
        # temp 있을 때, 현재 node의 다음 node에 새로운 node를 생성하고
        # 현재 node와 연결해준다.
        else:
            temp.next = ListNode(val)
            temp = temp.next

    return head


# 답안 접근
# 재귀 구조로 연결

def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    if (not l1) or (l2 and (l1.val > l2.val)):
        l1, l2 = l2, l1 # 다중할당
    if l1:
        l1.next = self.mergeTowLists(l1.next, l2)
    return l1
