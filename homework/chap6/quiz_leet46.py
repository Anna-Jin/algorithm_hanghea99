# 12장 그래프 - 34. 순열 (Permutations)
# 서로 다른 정수를 입력받아 가능한 모든 순열을 리턴하라
from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    # 결과를 담는 리스트
    results = []

    prev_elements = []

    def dfs(elements):
        # 마지막 노드일 때 결과 추가
        if len(elements) == 0:
            results.append(prev_elements[:])

        # 재귀 호출
        for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)

            prev_elements.append(e)
            dfs(next_elements)
            prev_elements.pop()

    # 함수 호출
    dfs(nums)
    return results


nums = [1, 2, 3]

print(permute(nums))