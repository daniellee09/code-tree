def find_leapyear(y):
    if y % 100 == 0 and y % 400 != 0:
        return False
    if y % 4 == 0:
        return True

y = int(input())
if find_leapyear(y):
    print("true")
else:
    print("false")