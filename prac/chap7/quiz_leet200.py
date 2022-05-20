# 12장 그래프 - 20. 섬의 개수 (Number of Islands)
# 1을 육지로, 0을 물로 가정한 2D 그리드 맵이 주어졌을 때, 섬의 개수를 계산하라.
# 연결되어 있는 1의 덩어리 개수를 구하라.


def island_dfs_recursive(grid):
    # 그리드에서 기준점을 상하좌우로 이동시키기 위한 변수
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    # 그리드의 전체 범위를 지정하는 함수
    rows, cols = len(grid), len(grid[0])

    # 섬의 개수를 세기 위한 변수
    cnt = 0

    # 재귀 함수
    def dfs_recursive(y, x):
        # 기준점이 grid를 벗어나거나, 섬이 아니면 skip
        if y < 0 or y >= rows or x < 0 or x >= cols or grid[y][x] != '1':
            return

        # 동서남북 노드 확인
        # 기준 노드 방문처리
        grid[y][x] = '0'
        for i in range(4):
            # 재귀
            dfs_recursive(y + dy[i], x + dx[i])
        return

    # 기준 노드를 하나씩 가져온다.
    for r in range(rows):
        for c in range(cols):
            node = grid[r][c]

            # 기준 노드가 섬이 아니면 skip
            if node != '1':
                continue

            # 섬 개수 카운팅
            cnt += 1
            dfs_recursive(r, c)

    return cnt


grid = [
    ["1", "1", "1", "1", "1", "1", "1"]
]

print(island_dfs_recursive(grid))

from collections import deque

def island_bfs(grid):
    # 그리드에서 기준점을 상하좌우로 이동시키기 위한 변수
    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]

    # 반복할 횟수
    rows, cols = len(grid), len(grid[0])

    # 섬의 개수
    cnt = 0

    for row in range(rows):
        for col in range(cols):
            # 섬이 아니면 skip
            if grid[row][col] != '1':
                continue

            cnt += 1

            # 시작점 세팅 / q는 기준점
            q = deque([(row, col)])

            while q:
                # 기준점을 꺼내준다.
                x, y = q.popleft()

                # 상하좌우가 섬인지 탐색
                for i in range(4):
                    nx = x + dx[i]  # 상 -1   하 1   좌 0     우 0
                    ny = y + dy[i]  # 상 0    하 0   좌 -1    우 1

                    # 이동시킨 점이 grid의 범위를 벗어나면 skip
                    if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] != '1':
                        continue

                    # 이미 탐색한 섬을 0으로 바꿔줌 -> 같은 곳을 다시 탐색하는 것 방지 (방문 표시)
                    grid[nx][ny] = '0'
                    q.append((nx, ny))

    # 섬 개수 반환
    return cnt


grid = [
    ["1", "1", "1", "1", "1", "1", "1"]
]

print(island_bfs(grid))
