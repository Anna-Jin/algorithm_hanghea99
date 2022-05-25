# 과목 수 n이 주어집니다.
# n개 과목의 학점을 입력받아서 평균학점을 구하여 출력하고, 평균이 4.0 이상이면 Perfect, 3.0 이상이면 Good, 3.0 미만이면 Poor를 출력하는 프로그램을 작성해보세요.

n = int(input())
score = list(map(float, input().split()))

sum = sum(score)

avg = sum / n

print(f"{avg:.1f}")

if avg >= 4.0:
    print('Perfect')
elif avg >= 3.0:
    print('Good')
else:
    print('Poor')