# 11장 해시 테이블 - 29. 보석과 돌 (Jewels-and-stones)
# J는 보석이며, S는 갖고 있는 돌이다. S에는 보석이 몇 개나 있을까? 대소문자는 구분한다.

# 내 접근
# 문제 - 해시 테이블을 이용하지 않은 풀이. 중첩 for문 사용.
# J와 S의 문자열을 하나씩 비교해서 서로 같다면 갯수를 센 다음 합해주는 간단한 풀이.
import collections

J = "z"
S = "ZZ"

def numJewelsInStones(J: str, S: str) -> int:
    sum = 0

    for j in J:
        count = 0

        for s in S:
            if j == s:
                count += 1

        sum += count

    return sum


# 풀이 접근
# 해시 테이블을 이용한 풀이
# 갖고 있는 돌 S의 각각 개수를 모두 해아린 다음, J의 각 요소를 키로 하는 각 개수를 합산한다.

def numJewelsInStones(J: str, S: str) -> int:
    # 테이블 선언
    freqs = {}

    for char in S:
        # 테이블 안에 char 인덱스가 없다면, 해당 인덱스를 생성하고 1을 넣어준다. char not in freqs는 key값이 있는 지 확인하는 조건문이다.
        if char not in freqs:
            freqs[char] = 1
        # 테이블 안에 char 인덱스가 있는데 또 같은 값이 들어왔다면, +1을 해준다.
        else:
            freqs[char] += 1

    count = 0
    for char in J:
        # 테이블 안에 해당 인덱스를 골라서 count에 합산해준다.
        if char in freqs:
            count += freqs[char]


    return count



# defaultdict()를 이용한 비교구문 생략
def numJewelsInStones(J: str, S: str) -> int:
    freqs = collections.defaultdict(int)
    count = 0

    for char in S:
        freqs[char] += 1

    for char in J:
         count += freqs[char]

    return count


# Counter()로 계산 생략
def numJewelsInStones(J: str, S: str) -> int:
    freqs = collections.Counter(S)
    count = 0

    for char in J:
        count += freqs[char]

    return count
