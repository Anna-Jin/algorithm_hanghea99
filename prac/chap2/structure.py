class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    # 헤더부터 탐색해 뒤에 새로운 노드 추가하기
    def append(self, data):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data)

    # 모든 노드 값 출력
    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        cnt = 0
        node = self.head
        while cnt < index:
            cnt += 1
            node = node.next
        return node

    def pop(self, data):
        temp = self.head
        if temp.data == data:
            del temp
            return
        else:
            while temp is not None:
                if temp.data == data:
                    break
                prev = temp
                temp = temp.next

            if temp is None: return
            prev.next = temp.next
            del temp
            return
