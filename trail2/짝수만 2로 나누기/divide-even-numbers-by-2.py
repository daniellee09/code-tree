n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def change_elem(arr):
    for i in range (len(arr)):
        if arr[i] %2 == 0:
            arr[i] = arr[i] // 2

change_elem(arr)
for elem in arr:
    print(elem, end=" ")