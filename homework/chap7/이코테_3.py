# 음료수 얼려먹기


# 입력
# 첫 번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어진다.
# 두 번재 줄부터 N + 1번째 줄까지 얼음 틀의 형태가 주어진다.
# 이때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1이다.

# n, m을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

print(n, m, graph)


# DFS로 특정한 노드를 방문한 뒤에 연결된 모드 노드들도 방문
def dfs(x, y):
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    rows, cols = len(graph), len(graph[0])

    cnt = 0

    for row in range(rows):
        pass
