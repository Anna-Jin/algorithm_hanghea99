# 8장 연결리스트 - 13. 팰린드롬 연결리스트  (리트코드 234)
# 연결리스트가 팰린드롬 구조인 지 판별하라

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
            self.head = ListNode(val, None) # head에 첫번째 값을 넣는다. 연결할 다음 노드는 없다.
        return

        # 비어있지 않는다면
        # 현재 바라보고 있는 노드를 head로 지정해준다.
        node = self.head

        # 마지막 노드(tail)로 이동해준다
        while node.next:
            node = node.next
        node.next = ListNode(val, None)


# 입력값
head = [1,2,2,1]


l1 = LinkedList()

for num in head:
    l1.append(num)

def isPalindrome(head):

    arr = []

    # head가 비어있다면 ture 반환
    if not head:
        return True

    node = head
    while node:
        # 배열에 node의 값을 넣는다.
        arr.append(node.val)
        # 다음 노드로 옮겨간다
        node = node.next

    while len(arr) > 1: # pop을 2개씩 하기 때문에 배열의 길이는 2 이상이어야함
        if arr.pop(0) != arr.pop():
            return False

    return True


