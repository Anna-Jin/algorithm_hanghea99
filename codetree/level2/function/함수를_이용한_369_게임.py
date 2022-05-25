# a에서 b사이에 숫자에 3, 6, 9 중에 하나가 들어가 있거나 그 숫자 자체가 3의 배수인 숫자의 개수를 세는 프로그램을 작성해보세요. 단, 함수를 이용하여 문제를 해결해주세요.


a, b = map(int, input().split())


def is_multiple(i):
    return (i % 3 == 0) or is_369(i)


def is_369(i):
    while i > 0:
        if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
            return True

        i //= 10

    return False


cnt = 0
for i in range(a, b + 1):
    if is_multiple(i):
        cnt += 1

print(cnt)
