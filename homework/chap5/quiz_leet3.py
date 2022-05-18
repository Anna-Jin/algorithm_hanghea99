# 11장 해시 테이블 - 30. 중복 문자 없는 가장 긴 부분 문자열 (Longest Substring WIthout Repeating Characters)
# 중복 문자가 없는 가장 긴 부분 문자열의 길이를 리턴하라

# 내 접근
# 포인터를 사용하면 어떨까?
import collections

s = "abcbbcbb"
s1 = "abccb"

# 풀이
# 슬라이딩 윈도우와 투 포인터로 사이즈 조절

def lengthOfLongestSubstring(s: str) -> int:
    # 새로운 해시 테이블 생성
    used = {}

    # 시작 포인터와 문자열의 최대 길이 설정
    max_length = start = 0
    for index, char in enumerate(s):
        # 뽑아온 문자가 테이블에 존재한다면 중복된 문자가 나타난 것이므로 start 포인터를 한칸 옮겨준다.
        if char in used and start <= used[char]:
            start = used[char] + 1

        # 뽑아온 문자가 테이블에 존재하지 않는다면, 지금까지 나왔던 가장 긴 문자열의 길이와 현재의 문자열 길이 중 큰 값으로 업데이트 해준다.
        # 여기서 index - start + 1은 현재 인덱스에서 지금까지 옮겨온 start의 길이를 빼고, 인덱스보다 길이가 1이 더 크므로 +1을 해준다.
        else:
            max_length = max(max_length, index - start + 1)

        # 현재 문자를 키로 하고 값에 현재 위치를 넣어준다. 이건 start 포인터를 움직이기 위해 사용한다.
        used[char] = index

    return max_length


print(lengthOfLongestSubstring(s))



