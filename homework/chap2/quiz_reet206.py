# 8장 연결리스트 - 15. 역순 연결 리스트
# 연결 리스트를 뒤집어라

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 내 접근
# head 노드 뒤에 prev를 두고 한칸씩 prev로 옮긴다.

def reverseList(head: ListNode) -> ListNode:
    node, prev = head, None

    while node:
        next, node.next = node.next, prev
        prev, node = node, next

    return prev

def reverseList(head: ListNode) -> ListNode:
    def reverse(node: ListNode, prev: ListNode) -> ListNode:
        # node가 없을 때, null을 반환
        if not node:
            return prev

        # next -> 다음노드, 다음 노드
        next, node.next = node.next, prev

        return reverse(next, node)
    return reverse(head)


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

reverseList(head)
