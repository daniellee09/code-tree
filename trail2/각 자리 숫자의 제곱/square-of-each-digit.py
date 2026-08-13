def print_square_sum(n):
    if n < 10:
        return n**2

    return print_square_sum(n//10)+((n%10)**2)

n = int(input())
print(print_square_sum(n))