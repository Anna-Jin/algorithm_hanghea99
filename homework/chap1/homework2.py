# 가장 긴 팰린드롬 부분 문자열
# 가장 긴 팰린드롬 부분 문자열을 출력하라.

# 입력

s = "babad"


# 팰린드롬 판별 및 투 포인터 확장
def expand(left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1:right]


if len(s) < 2 or s == s[::-1]:
    print(s)

result = ''

# 슬라이딩 윈도우 우측으로 이동
# range(len(s) - 1) -> s의 길이가 5일 때, 최소 2글자가 출력되려면 s[4:5]이므로 i의 최대값은 len(s) - 1 이다.
for i in range(len(s) - 1):
    result = max(result,
                 expand(i, i+1),    # 홀수일 때
                 expand(i, i+2),    # 짝수일 때
                 key=len)

print(result)