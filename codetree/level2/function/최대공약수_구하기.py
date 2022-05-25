# n, m이 주어졌을 때, n과 m의 최대공약수를 출력하는 프로그램을 작성해보세요.
# 단, 두 숫자를 인자로 받아 최대공약수를 구해 출력하는 함수를 만들어 문제를 해결해주세요.

# 12 18
#
# 1 2 3 4 6 12
# 1 2 3 6 9 12 18

n, m = map(int, input().split())

def find_gcd(n, m):
    gcd = 0

    for i in range(1, min(n, m) + 1):
        if n % i == 0 and m % i == 0:
            gcd = i

    print(gcd)

find_gcd(n, m)
