# leetcode 51. N-Queen

# 첫번째 - 강의 풀이
def nqueen(n):
    visited = [-1] * n
    answers = []

    def is_ok_on(nth_row):
        """
        n번째(nth) 행에 퀸을 놓았을 때, 올바른 수인지 검사한다.
        nth 행의 퀸 위치와, 0번째 행부터 n-1번째 행까지 놓여진 퀸의 위치를 비교한다.
        nth 행에 놓여진 퀸이 규칙을 깼다면 False 를 반환한다.
        """
        # 0번째 행 ~ nth_row-1번째 행의 퀸 위치를 차례대로 꺼내온다.
        # 영상에서 n-1이라고 말하는데 오류입니다. nth_row-1까지 살펴봅니다.
        for row in range(nth_row):
            # 방금 놓여진 nth 퀸은 (nth_row, visited[nth_row]) 에 놓여져있다.
            # 각 행에 차례대로 단 한 번만 두기 때문에 행이 겹치는 것은 검사하지 않아도 된다.
            # 1) 열 번호가 겹치지는 않는지? visited[nth_row] == visited[row]:
            # 2) 또는 대각선으로 존재하지는 않는지? nth_row - row == abs(visited[nth_row] - visited[row]) 살펴본다.
            if visited[nth_row] == visited[row] or nth_row - row == abs(visited[nth_row] - visited[row]):
                return False
        return True

    def dfs(row):
        """
        row 는 퀸을 놓을 행번호를 의미한다.
        dfs(0) 은 0번째 행에서 퀸의 위치를 고르는 것이고,
        dfs(1) 은 1번째 행에서 퀸의 위치를 고르는 것이고,
        ...
        dfs(n-1) 은 n-1번째 행에서 퀸의 위치를 고르는 것이다.
        따라서 row 는 n-1까지 가능하며, n이 되었다는 것은 n개의 퀸을 모두 올바른 위치에 두었다는 의미이다.
        """

        # 0 ~ n-1 행에 퀸을 모두 하나씩 두었을 때 경우의 수를 1 증가시키고 재귀탐색을 종료한다.
        if row >= n:
            answers.append(visited)
            print(visited)
            ################
            return

        # visited[row] 의 값을 결정한다.
        # n*n 의 체스판이므로 가능한 열의 범위는 0 ~ n-1 이다.
        for col in range(n):
            # (row, col) 위치에 퀸을 두었다고 가정하고, 규칙을 깨지 않는다면 row+1 행에 다시 퀸을 둔다.
            visited[row] = col
            if is_ok_on(row):
                dfs(row + 1)

    # 0번째 행에 퀸을 둔다.
    dfs(0)
    return answers

# nqueen(4)


def n_queen(n):
    visited = [-1] * n
    answers = []

    # 1) dfs구현
    def dfs(row):
        # 모든 경우의 수를 찾았을 때, answers에 결과값을 담고 리턴
        if row >= n:
            answers.append(visited)
            print(visited)
            return

        # visited[row]의 값을 결정한다 -> 퀸을 둔다.
        # 가능한 열의 범위는 0 ~ n - 1이다. 인덱스 번호는 0부터 시작하기 때문이다.
        # 열의 개수 만큼 반복 한다. 그 행의 열을 돌면서 어디다 퀸을 둘 지 판단해야하기 때문
        for col in range(n):
            visited[row] = col
            # 첫번째 줄에 퀸을 두었으면, 다음 줄에 퀸을 두러간다.
            # is_ok_on(row) -> 조건으로 주어진, 퀸이 다음 퀸을 잡지 못하는 위치를 판별하는 함수.
            if is_ok_on(row):
                # 첫번째 줄의 판별이 끝났다면 다음 줄에 퀸을 놓으러 간다.. ex) (0, 0) -> (1, 0)
                dfs(row + 1)

    # 퀸이 다른 퀸을 잡을 수 있는 지 판별하는 함수
    def is_ok_on(nth_row):
        for row in range(nth_row):
            # 퀸이 같은 세로줄에 있다면, 혹은 대각선에 있다면, False를 리턴
            # 대각선은 현재 놓여진 퀸과 새로 놓으려는 퀸의 행 간의 차이 == 열 간의 차이일 때, 판단가능 -> 그림으로 설명하기
            if visited[nth_row] == visited[row] or nth_row - row == abs(visited[nth_row] - visited[row]):
                return False

        # 세로줄과 대각선에 퀸이 놓여있지 않다면 다음 퀸을 놓으러 갈 수 있도록 True 리턴
        return True

    # 0번째 행에 퀸을 둔다.
    dfs(0)

    # 결과 리턴
    return answers

n_queen(4)