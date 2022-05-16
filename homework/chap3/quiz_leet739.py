# 9장 스택, 큐 - 22. 일일 온도
# 매일 화씨 온도(F) 리스트 T를 입력받아서, 더 따뜻한 날씨를 위해서는 며칠을 더 기다려야 하는지를 출력하라

# 내 접근
# 문제는 이해가 됐다. 현재 포인터 기준으로 포인터보다 큰 값이 몇번째 후에 있는 지 찾는 문제이다.
# 이제 이걸 stack으로 어떻게 접근하느냐... 모르겠으니 해답을 보자.
from typing import List

temperatures = [73,74,75,71,69,72,76,73]

# [1, 1, 4, 2, 1, 1, 0, 0]

def dailyTemperatures(temperatures: List[int]) -> List[int]:
    # 정답을 담기 위한 리스트 생성
    answer = [0] * len(temperatures)

    # 인덱스를 추가하기 위한 stack 생성
    stack = []

    # enumerate() 함수를 사용해서 인덱스와 값을 둘다 뽑아온다.
    for i, cur in enumerate(temperatures):
        # stack가 있으면서 현재의 온도가 전 날 온도보다 높은 경우
        while stack and cur > temperatures[stack[-1]]:
            # stack에 담아줬던 첫번째 날의 인덱스를 꺼내와서 last 변수에 담아준다.
            last = stack.pop()

            # answer의 last번째 인덱스에(이번 for문이 돌아가기 전 index가 last에 담겨있다.) 현재의 인덱스 - last 인덱스를 넣어준다.
            # i에 last를 빼주는 이유? while 조건에서 현재의 날씨가 전날의 날씨보다 낮은 경우 while문을 건너뛰고 stack에 계속 쌓아준다. stack의 pop은 stack에서 가장 마지막 엘리먼트를
            # 뽑아오므로 현재 날짜에서 n번 건너뛴 숫자가 현재 index - last 가 되는 것이다.
            answer[last] = i - last

        # stack(index)이 없을 때, stack에 현재 index를 추가해준다. 여기서 index를 추가해주는 이유는 while문 위에서 추가해주면 stack[-1]이 결국엔 자기 자신(i)이 된다.
        stack.append(i)

    return answer

# 고려해보기
# answer.append로 할 수 있는 방법이 있지 않을까?


print(dailyTemperatures(temperatures))



