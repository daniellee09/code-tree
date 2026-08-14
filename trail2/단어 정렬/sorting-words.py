n = int(input())
fruits = [input() for _ in range(n)]

sorted_fruits = sorted(fruits)
for elem in sorted_fruits:
    print(elem)