n = int(input())
numbers = [int(x) for x in input().split()][:n]
numbers.sort()

for elem in numbers:
    print(elem, end=' ')
print()
numbers.sort(reverse=True)
for elem in numbers:
    print(elem, end=' ')
