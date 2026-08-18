class Student:
    def __init__(self,height,weight,number):
        self.height = height
        self.weight = weight
        self.number = number
    
students = []
n = int(input())
for _ in range(n):
    height, weight = map(int,input().split())
    students.append(Student(height, weight, _+1))

students.sort(key=lambda x : (-x.height, -x.weight, x.number))

for student in students:
    print(student.height, student.weight, student.number)
