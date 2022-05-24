# # 정수 n의 값을 입력받아 별표를 출력하는 프로그램을 아래 예를 참고하여 작성해보세요.
#
# 예) n에 2를 입력받는 경우
#
# * *
# *

n = int(input())

for i in range(n):
	for _ in range(n-i):
		print("*", end=" ")
	print()