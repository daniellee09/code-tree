class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

people = []
for i in range(5):
    name, height, weight = input().split()
    people.append(Person(name, int(height), float(weight)))

people.sort(key=lambda x : x.name)

print("name")
for p in people:
    print(f"{p.name} {p.height} {p.weight:.1f}")
print()

people.sort(key=lambda x : -x.height)
print("height")
for p in people:
    print(f"{p.name} {p.height} {p.weight:.1f}")

