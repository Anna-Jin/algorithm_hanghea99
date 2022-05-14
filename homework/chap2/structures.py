class Node:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    # 헤더부터 탐색해 뒤에 새로운 노드 추가하기
    def append(self, data):
        if not self.head:
            self.head = Node(data, None)
            return

        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(data, None)

    def pop(self):
        node = self.head
        if self.head:
            if self.head.next is None:
                self.head = None
            else:
                while node.next.next:
                    node = node.next
                second_last = node
                node = node.next
                second_last.next = None
            return node.data


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




    def get_node(self, index):
        cnt = 0
        node = self.head
        while cnt < index:
            cnt += 1
            node = node.next
        return node

    def delete_node(self, data):
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

    def getSize(self):
        node = self.head
        count = 0
        while node is not None:
            node = node.next
            count += 1
        return count