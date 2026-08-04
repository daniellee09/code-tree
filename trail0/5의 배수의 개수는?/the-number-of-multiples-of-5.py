matrix = [[int(i) for i in input().split()] for _ in range(4)]
count = 0

for row in matrix:
    for elem in row:
        if elem % 5 == 0:
            count += 1

print(count)