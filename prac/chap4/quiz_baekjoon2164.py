# 백준 2164번 카드2
from collections import deque

N = int(input())
queue = []

for i in range(N, 0, -1):
    queue.append(i)

# 그림을 몇번 그려보면 짝수번 째 인덱스만 pop()되고, 홀수번 째 인덱스는 맨 아래로 옮겨진다.

for i in range(len(queue)):
    if len(queue) == 1:
        break

    queue.pop()


    while len(queue) > 1:
        temp = queue.pop()

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
    deq = deque([i for i in range(1, num + 1)])
    while len(deq) > 1:
        deq.popleft()
        deq.append(deq.popleft())
    return deq.popleft()


