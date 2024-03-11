class forecast:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

n = int(input())

arr = [tuple(input().split()) for _ in range(n)]
forecasts = [forecast(date,day,weather) for date, day, weather in arr]

rain =[]
rain_date = []
for i in range(n):
    if forecasts[i].weather == 'Rain':
        rain.append(forecasts[i])
        rain_date.append(forecasts[i].date)


min_idx = 0
for i in range(len(rain)):
    if rain_date[min_idx] > rain_date[i]:
        min_idx = i
        print(min_idx)

print(f"{rain[min_idx].date} {rain[min_idx].day} {rain[min_idx].weather}" )