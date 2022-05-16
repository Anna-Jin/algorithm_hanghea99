# 9장 스택, 큐 - 21. 중복 문자 제거
# 중복된 문자를 제외하고 사전식 순서로 나열하라.

# 내 접근
# 1. 스택을 사용하지 않고 해결
# set으로 중복 문자를 제거한 뒤, sort함수로 정렬 -> 알파벳 sort는 abc순서로 정렬된다.
import collections

s = "cbacbcbc"

b = sorted(''.join(set(s)))

# print(b)


# 출력이 다르다. 쉬운 문제인 줄 알았는데 난이도가 별 3개, medium이다. 사전식 순서라는 키워드에서 뭔가가 있는 것 같다.
# 사전식 순서에 대해 이해가 필요해서 해설을 봤는데도 이해를 못했다가 다른 수강생 분에게 질문을 하고 나서야 문제를 이해했다!!!
# 리트코드에서 문제를 보면 사전식으로 정렬하되, 가장 빠른 순으로 나열하라고 설명되어있다. (You must make sure your result is the smallest in lexicographical order among all possible results)
# 중복 제거와 사전식 순서가 함께 나오는 이유가 이제부터 나온다.
# 이 문제의 요점은, 중복을 제거 했을 때 나올 수 있는 가장 빠른 단어를 return하라 이다. 이렇게 해도 아직 이해가 안될 수 있다. 예시와 함께 이해해보자.
# ebcabc라는 입력값이 있다. 여기서 중복 문자는 b와 c이다. 만약 첫번째 b를 제거하면 ecabc가 나오고, 두번째 b를 제거하면 ebcac가 나온다.
# 이렇게 중복을 제거했을 때 나올 수 있는 모든 문자열 중에서 사전식 순서로 가장 빠른 값을 리턴하면 되는 문제이다.

# 이제 문제를 이해했으니 문제 풀이를 생각해보자.
# collections.Counter() -> 리스트의 개수를 세서 자동으로 딕셔너리로 만들어준다. 예를들어, [1,1,1,3,5,5,5]를 Counter 함수에 집어넣어주면
# {1: 3,  3: 1, 5: 3}를 반환해준다.

# 첫번째 풀이
def removeDuplicateLetters(s:str) -> str:
    # 문자열에서 각 알파벳의 개수를 센 후, 딕셔너리로 반환
    counter = collections.Counter(s)
    stack = []

    for char in s:
        # char하나를 꺼내 stack에 담을 지, 버릴 지 판별할 것이기 때문에 counter에서 글자 하나를 빼준다.
        counter[char] -= 1

        # 이미 해당 알파벳이 stack안에 있다면, continue를 해준다. 이 과정으로 중복을 건너뛰어준다.
        if char in stack:
            continue

        # stack에 값이 들어있고, 새로 뽑아온 문자가 stack에 들어있는 문자보다 작고, counter에 stack의 마지막 글자가 더 있으면 stack에서 꺼내준다.
        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            stack.pop()

        # stack에 알파벳을 넣어준다.
        stack.append(char)
    return ''.join(stack)


print(removeDuplicateLetters(s))


# 두번째 방법. 해설에서 정석이라고 설명한 방법. 스택은 스택의 기능만 담당하고, 안에 문자열이 있는 지 판별하는 건 set() 자료형인 seen 변수가 담당하게 한다.
def removeDuplicateLetters(s:str) -> str:
    counter = collections.Counter(s)
    seen = set()
    stack = []

    for char in s:
        counter[char] -= 1

        # seen 안에 해당 알파벳이 있는 지 검사. 중복을 제거해주는 과정이다.
        if char in seen:
            continue

        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            # seen에서 검색을 마쳤을 때, 조건을 만족하면 seen과 stack에서 모두 삭제해주고, 다음 과정으로 넘어간다.
            seen.remove(stack.pop())
        stack.append(char)
        seen.add(char)

    return ''.join(stack)