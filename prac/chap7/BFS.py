# BFS 구현하기
from collections import deque


def bfs(graph, start, visited):
    # 시작점을 담아준다
    queue = deque([start])

    # 방문처리
    visited[start] = True

    # 큐가 빌 때까지
    while queue:
        # 기준 노드
        v = queue.popleft()
        print(v, end=' ')
        # 그래프에서 방문처리한 노드와 연결된 인접노드들 탐색
        for i in graph[v]:
            # 방문한 적이 없는 원소들을 큐에 삽입
            if not visited[i]:
                queue.append(i)
                visited[i] = True


graph = [
    [],
    [2, 3, 8],
    [7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

bfs(graph, 1, visited)

