# 6장 문자열조작 - 06. 가장 긴 팰린드롬 부분 문자열
# 가장 긴 팰린드롬 부분 문자열을 출력하라.

# 입력

s = "babad"

# 팰린드롬 판별 및 투 포인터 확장
def expand(left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        # 투 포인터 확장
        # ex) left = 0, right = 0 + 1 일 때, s[left] = b, s[right] = a 이므로 포인터를 확장하지 않고 s[1:1]인 빈 값을 반환함
        # left = 1, right = 1 + 2 일 때, s[left] = a, s[right] = a 이므로 포인터를 확장시킨다.
        # 확장시키고 나면 s[left] = 0, s[right] = 4이고, s[left] = b, s[right] = d이므로 s[1:4]인 'ab'를 반환시킨다.
        left -= 1
        right += 1
    return s[left + 1:right]


# 해당 사항이 없을 때, 빠르게 리턴
if len(s) < 2 or s == s[::-1]:  # s[::-1] -> 문자열을 역순으로 배열
    print(s)

result = ''

# 슬라이딩 윈도우 우측으로 이동
# range(len(s) - 1) -> s의 길이가 5일 때, 최소 2글자가 출력되려면 s[4:5]이므로 i의 최대값은 len(s) - 1 이다.
for i in range(len(s) - 1):
    result = max(result,
                 expand(i, i + 1),  # 홀수일 때
                 expand(i, i + 2),  # 짝수일 때
                 key=len)

print(result)


# trouble shooting
# 내 접근
# 만약 "babad" 문자열이 주어졌을 때,
# 슬라이싱 기법으로 ba, ab, ba, ad / bab, aba, bad / baba, abad / babad로 나눠서 리스트에 담은 다음
# 각 항목을 일일히 뒤집은 다음에 기존 리스트의 같은 인덱스 데이터와 비교한다음 그 중에서 가장 긴 데이터를 리턴해주고자 했음.
# 하지만 이 방식은 중첩 for문을 사용해야하므로 O(n^2)의 복잡도를 가지므로 적합하지 않음.

# 답지 접근
# expand 함수를 이용