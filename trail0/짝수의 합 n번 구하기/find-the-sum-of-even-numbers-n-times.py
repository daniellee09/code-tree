n = int(input())
total = 0

for i in range(n):
    a, b = map(int, input().split())
    for j in range(a, b+1):
        if j%2 == 0:
            total += j
    print(total)
    total = 0