# 기본 함수
def f(x):
    return x * 2


print(f(3))

# lamda 이용
f = lambda x: x * 2
print(f(3))


# lamda를 이용한 객체 정렬
class Student:
    def __init__(self, kor, eng, math):
        self.kor = kor
        self.eng = eng
        self.math = math


students = [
    Student(90, 80, 90),  # 첫 번째 학생
    Student(20, 80, 80),  # 두 번째 학생
    Student(90, 30, 60),  # 세 번째 학생
    Student(60, 10, 50),  # 네 번째 학생
    Student(80, 20, 10),  # 다섯 번째 학생
]

students.sort(key=lambda x : x.kor)

for student in students:
    print(student.kor, student.eng, student.math)
