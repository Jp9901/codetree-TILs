class forecast:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

n = int(input())

arr = [tuple(input().split()) for _ in range(n)]
forecasts = [forecast(date,day,weather) for date, day, weather in arr]

for i in range(n):
    if forecasts[i].weather == 'Rain':
        rain = forecasts[i]
        break

print(f"{rain.date} {rain.day} {rain.weather}" )