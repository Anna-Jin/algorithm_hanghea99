# 그룹 애너그램
# 문자열 배열을 받아 애너그램 단위고 그룹핑하라.
import collections

strs = ["eat","tea","tan","ate","nat","bat"]

anagram = collections.defaultdict(list)

for word in strs:
    anagram[''.join(sorted(word))].append(word)

print(list(anagram.values()))