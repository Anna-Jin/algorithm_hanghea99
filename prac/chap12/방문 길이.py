def solution(dirs):
    move = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}

    visited = []

    x, y = 0, 0
    cnt = 0

    for command in dirs:
        dx, dy = move[command]

        # 그래프를 벗어났을 때
        if x > 5:
            x = 5

        if y > 5:
            y = 5

        if x < -5:
            x = -5

        if y < -5:
            y = -5

        nx, ny = x + dx, y + dy

        went = (x, y, nx, ny)
        back = (nx, ny, x, y)

        if went not in visited and\
                -5 <= x <= 5 and -5 <= y <= 5 and -5 <= nx <= 5 and -5 <= ny <= 5:
            visited.append(went)
            visited.append(back)
            cnt += 1

        x, y = nx, ny

    return cnt


print(solution("UUUUUUUUUUUDDDDDDDDDDDDDDDDDDDLLLLLLLLLLLLLLLLLRRRRRRRRRRRRRRRRR"))
