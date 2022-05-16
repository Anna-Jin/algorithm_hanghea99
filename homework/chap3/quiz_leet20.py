# 9장 스택, 큐 - 20. 유효한 괄호 (Valid Parentheses)
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.

# 괄호로 된 입력값이 올바른지 판별하라
# 괄호가 올바르게 열리고 닫혔는 지 판별하는 문제


# 내 접근
# pop으로 하나씩 꺼내서 비교하면 될 것 같다. 그런데 일일히 값을 비교해주면 너무 비효율적이다. 방법이 없을까?
# dict의 key와 value쌍이 있는 특징을 이용하면 되겠다. 이름이 dictionary인 것처럼 dict형을 사전처럼 사용해보자!


s = '()'

dict = {
    ')': '(',
    '}': '{',
    ']': '['
}

flag = False
def valid(s: str) -> bool:
    for char in s:
        if char in dict:
            flag = True
        else:
            flag = False

    return flag


print(valid(s)) # 틀렸을 때도 True반환. 조건문이 []쌍이 아니라 무조건 ]가 있는 지만을 판별하기 때문이다.

# 애초에 stack를 사용하지도 않았다. 이 코드는 없애버리자ㅋㅋㅋㅋㅋㅋㅋ


# 풀이 코드
def valid(s: str) -> bool:
    table = {
        ')': '(',
        '}': '{',
        ']': '['
    }

    stack = []

    for char in s:
        if char not in table:
            # dict에 char가 없으면 stack에 push한다 -> '({['를 넣어줌.
            stack.append(char)
        elif not stack or table[char] != stack.pop(): # 주의! 연산자의 우선순위에 신경쓸 것 (두 연결리스트의 병합에서도 나옴)
            return False

    return len(stack) == 0


def valid(s):
    pair = {
        '}': '{',
        ')': '(',
        ']': '[',
    }
    opener = "({["
    stack = []

    for char in s:
        if char in opener:
            stack.append(char)
        else:
            if not stack:
                return False
            top = stack.pop()
            if pair[char] != top:
                return False

    return not stack
