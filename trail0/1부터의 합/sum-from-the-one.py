n = int(input())
sum = 0
cnt = 0

for i in range(1, 101):
    if sum >= n:
        break
    sum += i
    cnt = i

print(cnt)