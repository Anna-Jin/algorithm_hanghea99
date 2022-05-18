# 해시 테이블
# 키를 값에 매핑할 수 있는 구조인, 연관 배열 추상 자료형(ADT)를 구현하는 자료구조이다.

# 테스트 할 수 있는 코드 - 해시테이블 구현 후 import해서 사용 가능
# def test_hashtable():
#     ht = MyHashTable()
#
#     ht.put(1, 1)
#     ht.put(2, 2)
#     assert ht.get(1) == 1
#     assert ht.get(3) == -1
#
#     ht.put(2, 1)
#     assert ht.get(2) == 1
#
#     ht.remove(2)
#     assert ht.get(2) == -1
#
#
# def test_birthday_problem():
#     import random
#     TRIALS = 100000
#     same_birthdays = 0
#
#     for _ in range(TRIALS):
#         birthdays = []
#         for i in range(23):
#             birthday = random.randint(1, 365)
#             if birthday in birthdays:
#                 same_birthdays += 1
#                 break
#             birthdays.append(birthday)
#
#     print(f"{same_birthdays / TRIALS * 100}%")
#
#
# if __name__ == "__main__":
#     test_birthday_problem()
#     test_hashtable()
