# 깊이 우선 탐색 (DFS, Depth First Search)

# 재귀 구조로 구현한 슈도 코드(의사코드, pseudocode)
# 슈도 코드란?프로그램을 작성할 때 각 모듈이 작동하는 논리를 표현아기 위한 언어이다. 특정 프로그래밍 언어의 문법에 따라 쓰인 것이 아니라, 일반적인  언어로 코드를 흉내 내어 알고리즘을 써놓은 코드를 말한다.

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


def dfs_recursive(graph, v, visited):
    visited[v] = True

    print(v, end=' ')

    for i in graph[v]:
        if not visited[i]:
            dfs_recursive(graph, i, visited)


def dfs_stack(start):
    visited = []
    # 방문할 순서를 담아두는 용도
    stack = [start]

    # 방문할 노드가 남아있는 한 아래 로직을 반복한다.
    while stack:
        # 제일 최근에 삽입된 노드를 꺼내고 방문처리한다.
        top = stack.pop()
        visited.append(top)
        # 인접 노드를 방문한다.
        for adj in graph[top]:
            if adj not in visited:
                stack.append(adj)

    return visited


assert dfs_recursive(1, []) == [1, 2, 5, 6, 7, 3, 4]
assert dfs_stack(1) == [1, 4, 3, 5, 7, 6, 2]