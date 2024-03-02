i = 0
sum_val = 0
while 1:
    n = int(input())
    if n >= 30 or n < 20:
        break
    i += 1
    sum_val += n
print(f"{sum_val/i:.2f}")