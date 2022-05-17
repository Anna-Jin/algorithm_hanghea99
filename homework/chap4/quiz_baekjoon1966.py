# 백준 1966번 프린터큐
import collections

num_case = int(input())  # 테스트 케이스 횟수

for _ in range(num_case):
    N, M = map(int, input().split())  # N = 문서의 개수, M = 몇 번째로 인쇄되었는 지 궁금한 문저가 현재 Queue에서 몇 번째에 놓여있는 지 나타내는 정수
    important = list(map(int, input().split()))[:N]
    find_num = important[M]
    deq = collections.deque(important)

    count = 0

    while len(deq) > 0:
        num = deq.popleft()

        if deq or num < max(deq):
            # 제일 앞에 숫자를 맨 뒤로 보내준다.
            deq.append(num)
        elif not deq or num > max(deq):
            count += 1
            if num == find_num:
                break

    print(count)