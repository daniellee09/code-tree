m1,d1,m2,d2 = map(int, input().split())
A = input()

days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

date1 = sum(days[:m1]) + d1
date2 = sum(days[:m2]) + d2

start = 0
diff = date2 - date1

count = 0
for i in range(diff+1):
    now = week[(start+i) % 7]

    if now == A:
        count += 1

print(count)
    