# leet 3. Longest Substring Without Repeating Characters
# interview 30. 중복 문자 없는 가장 긴 부분 문자열

# 중복 문자가 없는 가장 긴 문자열을 찾아라

s = "abcabcbb"


def longest(s):
    left = 0
    word = ''
    result = 0

    for i in range(len(s)):
        right = i + 1

        if right >= len(s):
            break

        word += s[left]
        left = len(word) - 1

        if s[right] in word:
            result = len(word) - 1
            word = ''
            continue

    return result


print(longest(s))