a, b = map(int, input().split())
n = list(map(int,input()))
# Please write your code here.
# 먼저 A진수의 N을 10진수로 변환
num = 0
for i in range(len(n)):
    num = num * a + n[i]

# 이제 변환된 num을 다시 B진수로
arr = []
while True:
    if num < b:
        arr.append(num)
        break
    arr.append(num%b)
    num //= b

for i in arr[::-1]:
    print(i, end="")

    