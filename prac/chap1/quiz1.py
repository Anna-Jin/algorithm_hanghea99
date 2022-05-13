# 알파벳 소문자로만 이루어진 단어 S가 주어진다.
# 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를,
# 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.


# 내 풀이 - 백준 제출용
S = input()
alpabet = 'abcdefghijklmnopqrstuvwxyz'
for i in alpabet:
    if i in S:
        print(str(S.index(i)), end=' ')
    else:
        print(str(-1), end=' ')


# 강의 풀이
import string

# point: ord -> 문자를 아스키코드로 변환해주는 함수
S = input()
result = [-1]*len(string.ascii_lowercase)
for i in range(len(S)):
    idx = ord(S[i]) - 97
    if result[idx] == -1:
        result[idx] = i
print(' '.join([str(num) for num in result]))
