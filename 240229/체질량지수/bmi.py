h,w = map(int, input().split())

bmi = int(w//((h/100)**2))
print(bmi)
if bmi >= 25:
    print('Obesity')