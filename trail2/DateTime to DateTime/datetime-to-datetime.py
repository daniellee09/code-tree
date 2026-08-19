a,b,c = map(int, input().split())

day_to_hour = (a-11)*1440 + (b*60) # 11일부터 A일 b시까지의 총 분
hours_to_min = (11*60) # 11시간 빼주기 
mins = c-11

duration = day_to_hour - hours_to_min + mins

if duration < 0:
    print(-1)
else: 
    print(duration)

