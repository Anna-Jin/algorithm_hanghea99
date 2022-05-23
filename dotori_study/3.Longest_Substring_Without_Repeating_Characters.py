# leet 3. Longest Substring Without Repeating Characters
# interview 30. 중복 문자 없는 가장 긴 부분 문자열

# 중복 문자가 없는 가장 긴 문자열을 찾아라

s = "abcabcbb"


def longest(s):
    answer = 0
    left = 0
    used = {}

    for right, char in enumerate(s):
        # used 안에 단어가 있고, 오른쪽 포인터(used[char])가 왼쪽 포인터 보다 작다면
        # 왼쪽 포인터를 한칸 옮겨준다.
        if char in used and left <= used[char]:
            left = used[char] + 1
        # 그렇지 않다면 최대 길이를 구해준다.
        else:
            answer = max(answer, right - left + 1)

        used[char] = right

    return answer


print(longest(s))