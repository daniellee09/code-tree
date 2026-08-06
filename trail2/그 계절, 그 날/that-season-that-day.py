def find_leap(y):
    if y%100 == 0 and y%400 != 0:
        return False
    if y % 4 == 0:
        return True

def exist_day(y,m,d):
    if m in [4,6,9,11] and d > 30:
            return False
    elif m == 2:
        if find_leap(y):
            if d > 29:
                return False
        else:
            if d > 28:
                return False
    else:
        if d > 31:
            return False
    return True

def season(m):
    if m in [3,4,5]:
        print("Spring")
    elif m in [6,7,8]:
        print("Summer")
    elif m in [9,10,11]:
        print("Fall")
    else:
        print("Winter")


def find_season(y,m,d):
    # m에 따라 계절을 구분한다
    # y가 윤년인지 판단한다 -> 윤년이면 2월이 29일까지
    # d가 m에 존재하는(유효한) 날인지 판단한다
    if exist_day(y,m,d):
        season(m)
    else:
        print(-1)


y,m,d = map(int, input().split())
find_season(y,m,d)
