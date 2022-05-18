# 11장 해시 테이블 - 706. 해시맵 디자인 (Design HashMap)
# 다음의 기능을 제공하는 해시맵을 디자인하라.

# put(key, value) - 키, 값을 해시맵에 삽입. 만약 이미 존재 하는 키라면 업데이트할 것
# get(key) - 키에 해당하는 값을 조회. 만약 키가 존재 하지 않는다면 -1을 리턴할 것
# remove(key) - 키에 해당하는 키, 값을 해시맵에서 삭제

# 개별 체이닝 방식을 이용한 해시 테이블 구현
import collections


class MyHashMap:
    # 초기화
    def __init__(self):
        # 기본 사이즈 설정
        self.size = 1000000
        # 존재하지 않는 키를 조회할 경우 자동으로 기본 딕셔너리를 생성해주는 defaultdict 사용 -> 왜?
        self.table = collections.defaultdict(ListNode)

    def put(self, key: int, value: int) -> None:
        # 모듈로 연산을 한 나머지를 해시값으로 지정해주기로 한다. 가장 기본적인 해싱 방식임!
        # 모듈로 연산? 어떤 한 숫자를 다른 숫자로 나눈 나머지를 구하는 연산.
        index = key % self.size # 테이블의 인덱스

        # self.table[index] is None이 아니라 self.table[index].val is None으로 value의 존재 유무를 비교하는 이유?
        # 위에서 선언한 self.table이 collections.defaultdict(ListNode)는 존재하지 않는 인덱스로 조회 시 바로 디폴트 딕셔너리를 생성해주는 특성때문이다.
        # self.table[index].value 는 self.table에서 [index]를 조회해서 value를 가져온다. 이 부분이 인덱스로 조회하는 부분이고, 이 코드가 실행되었을 때,
        # 만약 일반 딕셔너리였을 때, 해당 인덱스가 존재하지 않으면 에러를 뱉어내지만 defaultdict()로 인해 즉시 새로운 디폴트 딕셔너리를 만들어준다.
        # self.table[index] is None 이었다면 인덱스와 매칭되는 value를 찾는 시도 없이 바로 해당 부분에 값을 넣으려는 시도를 하기 때문에 에러가 난다..?
        if self.table[index].value is None: # defaultdict 생성, collections.defaultdict(ListNode)로 생성했기 때문에 해당 인덱스와 매칭되는 value에 빈 ListNode가 생성됨
            self.table[index] = ListNode(key, value) # 비어있는 공간에 요소 추가
            return

        p = self.table[index]
        while p: # 인덱스의 첫번째 값

            # 종료 조건 1 - 테이블에 노드가 있을 때
            # 키 값이 같은 노드 찾기
            if p.key == key:
                # 키 값이 같은 노드에 값 업데이트 후 종료
                p.value = value
                return
            # 종료조건 2 - 다음 노드에 값이 없을 때
            # 이 코드가 없으면 p = p.next가 됐을 때, while문을 탈출하고, p.next에는 아무것도 없기 때문에 다음 코드(p.next = ListNode(key, value))로 넘어갔을 때 에러가 난다.
            if p.next is None:
                break
            p = p.next

        p.next = ListNode(key, value)


    def get(self, key: int) -> int:
        index = key % self.size
        # 찾을 키가 없으면 -1 리턴
        if self.table[index].value is None:
            return -1

        p = self.table[index]
        while p:
            # 키 값과 매칭되는 요소 찾기
            if p.key == key:
                return p.value
            p = p.next

        # 찾아봤는데도 없다면 -1 리턴
        return -1

    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            return

        p = self.table[index]

        # 인덱스의 첫번째 노드일 때. while로 p.next를 해주지 않았으니 첫번째 노드만 비교한다.
        if p.key == key:
            # 인덱스에 들어있는 노드가 하나뿐이면 해당 노드를 빈 노드로 바꿔준다.
            if p.next is None: # p.next가 None이라는 말이 첫번째 노드라는 말과 같다.
                # 빈 노드로 바꿔주는 이유? None으로 바꾸면 if self.table[index].value is None 코드에서 table[index] 자체가 None이기 때문에 .value를 수행할 수 없어서 에러가 남
                # 해시 테이블 객체를 생성하거나 추가하려는데 키 값이 없어서 if self.table[index].value is None 조건문을 탈 때에 self.table[index]는 자동으로 ListNode()로 생성되기 때문에
                # 이 조건문에서 현재의 노드를 처음 상태로 되돌려주는 것이다.
                self.table[index] = ListNode()
                return


        # 연결 리스트 노드 삭제
        prev = p
        while p:
            # 해당 키를 검색.
            if p.key == key:
                # 현재 노드의 다음노드와 현재 노드의 이전 노드를 연결해 줌으로써 현재노드의 연결을 끊는다. 왜 이렇게 되나요? 첫번째 노드는 이미 위에서 걸러지고,
                # 2번째부터는 값이 있다고 했을 때, prev에는 반복문 돌기 전 현재노드 즉, 다음 반복문에서는 이전노드가 담기고 p에는 다음 노드가 담기기 때문이다.
                prev.next = p.next
            prev = p
            p = p.next

# 개별 체이닝 방식을 이용하기 위해 연결 리스트 클래스 구현
class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


