class Person:
    def __init__(self, name, h, w):
        self.name = name
        self.h = h
        self.w = w

n = int(input())
people = []

for i in range(n):
    n, h, w = input().split()
    people.append(Person(n, int(h), int(w)))

people.sort(key=lambda x : (x.h, -x.w))

for p in people:
    print(p.name, p.h, p.w)
