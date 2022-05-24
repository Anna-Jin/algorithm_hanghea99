# 정수 n이 주어졌을 때, 1부터 차례대로 100까지 1씩 증가시키며 합을 구하다가 처음으로 그 합이 n 이상이 되는 순간에 더해진 숫자가 무엇인지를 출력하는 프로그램을 작성해보세요.


n = int(input())

sum = 0

for i in range(1, 101):
    sum += i
    if sum >= n:
        print(i)
        break




