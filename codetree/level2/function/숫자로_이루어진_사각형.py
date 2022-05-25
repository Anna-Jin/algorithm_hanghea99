# 정수 N의 값이 주어지면 일의자리 숫자로 이루어진 N * N 모양 사각형을 출력하는 프로그램을 작성해보세요.
# 이때 정수 n을 전달받아 일의 자리 숫자로 이루어진 정사각형을 출력하는 함수를 작성하고, 주어진 N을 함수로 전달하여 출력합니다.

n = int(input())

def print_rectangle(n):
    cnt = 1
    for _ in range(n):
        for _ in range(n):
            print(cnt, end=' ')
            cnt += 1
            if cnt == 10:
                cnt = 1
        print()

print_rectangle(n)