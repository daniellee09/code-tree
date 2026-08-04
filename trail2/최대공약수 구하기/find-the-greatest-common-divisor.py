def gcd(n,m):
    while m > 0:
        n, m = m, n%m
    return n
    

n,m = map(int, input().split())
print(gcd(n,m))
