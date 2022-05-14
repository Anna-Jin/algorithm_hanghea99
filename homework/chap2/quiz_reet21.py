# 8장 연결리스트 - 14. 두 정렬 리스트의 병합
# 정렬되어 있는 두 연결 리스트를 합쳐라

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# 내 접근
# 두 리스트의 데이터를 하나씩 꺼내서 배열에 담아 정렬한 다음 새로운 리스트에 담는다.
class Solution:
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

        node = None
        result = None  # 새로 만든 리스트

        for val in sorted(l):
            # node가 없을 때, 새로운 node를 생성하고 result에 담는다.
            if not node:
                node = ListNode(val)
                result = node
            # node가 있을 때, 현재 node의 다음 node에 새로운 node를 생성하고 현재 node와 연결해준다.
            else:
                node.next = ListNode(val)
                node = node.next

        return result


# 답안 접근
# 재귀 구조로 연결

def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    if (not l1) or (l2 and l1.val > l2.val):
        l1, l2 = l2, l1 # 다중할당
    if l1:
        l1.next = self.mergeTowLists(l1.next, l2)
    return l1
