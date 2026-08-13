count = 0
def print_count(n):
    global count
    if n == 1:
        return count


    if n % 2 == 0:
        count += 1
        return print_count(n//2)
    else:
        count += 1
        return print_count(n//3)

n = int(input())
print(print_count(n))