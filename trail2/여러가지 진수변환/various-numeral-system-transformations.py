N, B = map(int, input().split())
arr = []
# Please write your code here.
while True:

    if N < B:
        arr.append(N)
        break
    
    arr.append(N%B)
    N //= B

for i in arr[::-1]:
    print(i, end="")
