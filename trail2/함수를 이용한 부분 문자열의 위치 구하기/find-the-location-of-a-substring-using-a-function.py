n = input()
m = input()

def find_m():
    for i in range(len(n)-len(m)+1):
        if n[i:i+len(m)] == m:
            return i
    return -1

print(find_m())
        