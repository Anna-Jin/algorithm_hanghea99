# 7장 배열 - 09. 세 수의 합
# 배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라


nums = [-1, 0, 1, 2, -1, -4]
nums.sort()

# 첫번째 방식 - 중첩 for문 사용하기 (브루트 포스) -> 리트코드에서 time limit exeeded

results = []
# i는 index(3)까지 이동함. (뒤에 숫자 2개가 남아있어야하니까)
for i in range(len(nums) - 2):
    # j는 index(4)까지 이동함
    # 중복제거
    if i > 0 and nums[i] == nums[i - 1]:
        continue
    for j in range(i + 1, len(nums) - 1):
        if j > i + 1 and nums[j] == nums[j - 1]:
            continue
        for k in range(j + 1, len(nums)):
            if k > j + 1 and nums[k] == nums[k - 1]:
                continue
            if nums[i] + nums[j] + nums[k] == 0:
                results.append([nums[i], nums[j], nums[k]])

print(results)


# 두번째 - 투포인터 사용하기
# 투포인터란?
# 시작점과 끝점 혹은 left와 right 포인터 두 지점을 기준으로 하는 문제풀이 전략. for문을 줄이기 위해서 사용한다.

for i in range(len(nums) - 1):
    # 중복 제거
    if i > 0 and nums[i] == nums[i - 1]:
       continue

    # 투 포인터 설정
    left, right = i + 1, len(nums) - 1

    sum = nums[i] + nums[left] + nums[right]

    # 합계가 0보다 클 때, 제일 큰 수인 nums[right]을 왼쪽(작은 수)로 옮긴다.
    if sum > 0:
        right -= 1
    # 합계가 0보다 작을 때, 제일 작은 수인 nums[left]를 오른쪽(큰 수)로 옮긴다.
    elif sum < 0:
        left += 1
    # 합계가 0일 때, results에 넣는다. 이때,
    else:
        results.append([nums[i], nums[left], nums[right]])

print(results)