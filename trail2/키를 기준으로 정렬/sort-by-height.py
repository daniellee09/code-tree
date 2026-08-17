n = int(input())
people = []
for _ in range(n):
    name, height, weight = input().split()
    people.append((name, int(height), int(weight)))

people.sort(key=lambda x : x[1])

for p in people:
    print(p[0], p[1], p[2])