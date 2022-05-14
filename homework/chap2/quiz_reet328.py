# 8장 연결리스트 - 18. 홀짝 연결 리스트
# 연결 리스트를 홀수 노드 다음에 짝수 노드가 오도록 재구성하라. 공간 복잡도 O(1), 시간 복잡도 O(n)에 풀이하라.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 내 접근
# 리스트의 index(0)은 홀수이고 index(1)은 짝수이다. 그리고 두 칸씩 건너뜀. head.next.next를 반복하면 되지 않을까?

def oddEvenList(head: ListNode) -> ListNode:
    # 예외 처리
    if head is None:
        return None

    odd = head
    even = head.next
    even_head = head.next

    # odd가 있을 때까지 반복
    while even and even.next:
        # odd와 even의 다음
        odd.next, even.next = odd.next.next, even.next.next

        # odd와 even을 다음으로 옮겨준다.
        odd, even = odd.next, even.next

    odd.next = even_head

    return head


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

oddEvenList(head)