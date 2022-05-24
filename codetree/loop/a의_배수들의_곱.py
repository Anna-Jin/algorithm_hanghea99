# 두 정수 a와 b가 주어졌을 때, 1부터 b까지의 수 중 a의 배수들의 곱을 구하는 프로그램을 작성해보세요.


a, b = map(int, input().split(' '))

prod = 1
for i in range(1, b + 1):
    if i % a == 0:
        prod *= i

print(prod)