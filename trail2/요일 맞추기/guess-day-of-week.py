m1,d1,m2,d2 = map(int, input().split())

days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

date1 = sum(days[:m1]) + d1
date2 = sum(days[:m2]) + d2

week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

diff = date2 - date1

answer = week[diff%7]

print(answer)