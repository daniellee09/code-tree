a = input()

def palindrome(strs):
    return strs == strs[::-1]

if palindrome(a):
    print("Yes")
else:
    print("No")