class Student:
    def __init__(self,h,w, num):
        self.h = h
        self.w = w
        self.num = num

st = []
n = int(input())
for i in range(n):
    h, w = map(int,input().split())
    st.append(Student(h,w,i+1))

st.sort(key=lambda x: (x.h, -x.w))

for s in st:
    print(s.h, s.w, s.num)
