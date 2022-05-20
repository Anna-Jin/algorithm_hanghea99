# 12장 그래프 - 20. 섬의 개수 (Number of Islands)
# 1을 육지로, 0을 물로 가정한 2D 그리드 맵이 주어졌을 때, 섬의 개수를 계산하라.
# 연결되어 있는 1의 덩어리 개수를 구하라.
import collections
from typing import List

from collections import deque


def island_bfs(grid):
    # 그리드에서 기준점을 상하좌우로 이동시키기 위한 변수
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    # 시작점
    rows, cols = len(grid), len(grid[0])

    # 섬의 개수
    cnt = 0

    for row in range(rows):
        for col in range(cols):
            # 섬이 아니면 skip
            if grid[row] != '1':
                continue

            cnt += 1

            # 시작점 세팅 / q는 기준점
            q = deque([(row, col)])

            while q:
                # 기준점을 꺼내준다.
                x, y = q.popleft()

                # 상하좌우가 섬인지 탐색
                for i in range(4):
                    nx = x + dx[i]  # 상 0    하 0   좌 -1    우 1
                    ny = y + dy[i]  # 상 -1   하 1   좌 0     우 0

                    # 이동시킨 점이 grid의 범위를 벗어나면 skip
                    if (nx < 0 or nx >= rows) or (ny < 0 or ny >= cols) or grid[nx] != '1':
                        continue

                    # 이미 탐색한 섬을 0으로 바꿔줌 -> 같은 곳을 다시 탐색하는 것 방지 (방문 표시)
                    grid[nx][ny] = '0'
                    q.append((nx, ny))

    # 섬 개수 반환
    return cnt