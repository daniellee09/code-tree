n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
offset = 100
num = [0] * 200
for start, end in segments:
    for i in range(start, end):
        num[i + offset] += 1

print(max(num))
        
