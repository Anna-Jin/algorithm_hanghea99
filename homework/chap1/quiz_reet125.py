# 6장 문자열 조작 - 01. 유효한 팰린드롬
# 주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.
# 팰린드롬? 앞뒤가 똑같은 단어나 문장으로, 뒤집어도 같은 말이 되는 단어 또는 문장.

# ex)
# 입력 - "A man, a plan, a canal: Panama"
# 출력 - true

# 힌트 - isalnum() : 영문자, 숫자를 판별하는 함수

# 입력
s = "A man, a plan, a canal: Panama"

# 나눈 문자열을 담을 리스트
strs = []
for char in s:
    # 영문자, 숫자를 판별하는 함수
    if char.isalnum():
        # 문자열을 한글자씩 쪼개서 strs에 담는다.
        strs.append(char.lower())

# strs 뒤집기
reversed_strs = list(reversed(strs))

# 같은지 판단하는 트리거
flag = True
for i in range(len(strs)):
    if strs[i] == reversed_strs[i]:
        flag = True
    else:
        # strs와 뒤집힌 strs의 단어가 다르면 트리거를 false로 바꾸고 반복문 종료
        flag = False
        break


print(flag)

# trouble shooting
# 새롭게 알게 된 부분 - isalnum() : 영문자, 숫자를 판별하는 함수