# 백준 2164번 카드2
from collections import deque

N = int(input())
queue = []

for i in range(N, 0, -1):
    queue.append(i)

# 그림을 몇번 그려보면 짝수번 째 인덱스만 pop()되고, 홀수번 째 인덱스는 맨 아래로 옮겨진다는 걸 알 수 있다.

for i in range(len(queue)):
    if len(queue) == 1:
        break

    queue.pop()

    while len(queue) > 1:
        temp = queue.pop()

        # 잘못짠 코드 - 이미 pop해버린 temp를 다시 queue의 맨 앞에 넣어보려고 했으나 실패했다. 그냥 reverse했다가 append하고 다시 reverse하는 방식도 생각해봐야겠다.
        if i + 1 < len(queue):
            last = queue[i+1]
            queue[i+1] = queue[i]
            queue[i] = last
            i += 1

    queue[0] = temp


print(queue)


# 어느 부분에서 틀린 지 모르겠다. 해설을 보자
# 데크를 사용한 방식. 데크란? 양쪽 끝에서 빠르게 추가 삭제를 할 수있는 리스트류 컨테이너
def test_problem_queue(num):
    # 리스트 컴프리헨션 - 한 줄로 리스트를 만드는 방식.
    # 풀어쓰면 다음과 같다
    # list = []
    # for i in range(1, num + 1):
    #   list.append(i)
    deq = deque([i for i in range(1, num + 1)]) # ex) [1, 2, 3, 4]
    while len(deq) > 1:
        deq.popleft() # 맨 첫번째 (왼쪽) 요소 꺼내기 - 위에서 부터 1234의 순서로 놓여있다고 했으므로 제일 왼쪽 요소가 제일 위쪽에 있다고 본다.
        deq.append(deq.popleft())
    return deq.popleft()


