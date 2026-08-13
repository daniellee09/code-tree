def pibonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    
    return pibonacci(n-1) + pibonacci(n-2)

n = int(input())

print(pibonacci(n))