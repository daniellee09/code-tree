n = int(input())

def divide_ten(n):
    total = 0
    for i in range(1,n+1):
        total+=i
    return total//10

result = divide_ten(n)
print(result)
        