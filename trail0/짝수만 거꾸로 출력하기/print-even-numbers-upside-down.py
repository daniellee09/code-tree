n = int(input())
num = list(map(int, input().split()))
new = []

for i in num:
    if i % 2 == 0:
        new.append(i)

new.reverse()

for j in new:
    print(j, end=' ')