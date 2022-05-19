# 전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
# 전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.
# 구조대 : 119
# 박준영 : 97 674 223
# 지영석 : 11 9552 4421
# 전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때,
# 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

phone_book = ["119", "97674223", "1195524421"]

def solution(phone_book):
    # 정렬하면 맨 앞에 길이가 제일 작은 숫자가 오게 되므로 전체를 비교할 필요가 없어진다.
    phone_book.sort()

    # 맨 앞의 요소를 기준으로 prefix가 있는 지 검사하기
    for num1, num2 in zip(phone_book, phone_book[1:]):
        if num2.startswith(num1):
            return False
    return True

print(solution(phone_book))

