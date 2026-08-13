def print_sum(n):
    if n > 0:
        return print_sum(n-1)+n
    else:
        return 0

n = int(input())
print(print_sum(n))