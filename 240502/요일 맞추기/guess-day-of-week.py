m1, d1, m2, d2 = map(int,input().split())

day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat','Sun']
num_of_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

elapsed_day = 0

if m1 > m2 :
    elapsed_day = d1+(num_of_days[m2]-d2)
elif m1 == m2:
    elapsed_day = d2-d1
else:
    elapsed_day = (sum(num_of_days[m1:m2])-d1)+d2


print(day[elapsed_day%7])