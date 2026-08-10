n,m = map(int,input().split())
a = list(map(int,input().split()))

# def func1(a,m):
#     total = 0
#     while m > 0:
#         total += a[m-1]
#         if m % 2 == 0:
#             m //= 2
#         else:
#             m -= 1
        
#     return total

# print(func1(a,m))

def get_answer():
    global m

    total = 0
    while m:
        total += a[m-1]

        if m % 2 == 0:
            m //= 2
        else:
            m -= 1
    return total

print(get_answer())
        
