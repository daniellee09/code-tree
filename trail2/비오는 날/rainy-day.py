class Weather:
    def __init__(self, date="", day="", weather=""):
        self.date = date
        self.day = day
        self.weather = weather

n = int(input())

weathers = []
for _ in range(n):
    date, day, weather = tuple(input().split())
    if weather == "Rain":
        weathers.append(Weather(date,day,weather))

weathers = sorted(weathers, key = lambda x: x.date)

print(weathers[0].date, weathers[0].day, weathers[0].weather)
    
