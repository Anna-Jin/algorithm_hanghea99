# 그룹 애너그램
# 문자열 배열을 받아 애너그램 단위고 그룹핑하라.
import collections

strs = ["eat","tea","tan","ate","nat","bat"]

anagram = collections.defaultdict(list)

for word in strs:
    anagram[''.join(sorted(word))].append(word)

print(list(anagram.values()))

# trouble shooting
# 첫 알고리즘 도전 부분이라 개념과 새로운 부분만 이해했음. 과제톡 발표로 보충할 것
# 새로 알게 된 함수 - collections.defaultdict()
# 쉽게 말하면 딕셔너리에 key값을 지정해주지 않아도 딕셔너리를 만들 수 있게 해주는 함


# 추가로 고려해야하는 점 -> 무엇을 기준으로 정렬되는지? 영문으로 정렬되는지, 한글일 때 인코딩문제는 없는지?




