class Student:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

n = int(input())

stu = []
for _ in range(n):
    name, kor, eng, math = input().split()
    # student 객체를 생성하여 리스트에 추가
    stu.append(Student(name, int(kor), int(eng), int(math)))

# 점수 내림차순 정렬 (국어 -> 영어 -> 수학)
stu.sort(key=lambda x: (-x.kor, -x.eng, -x.math))

# 반복 변수 s의 속성 출력
for s in stu:
    print(s.name, s.kor, s.eng, s.math)