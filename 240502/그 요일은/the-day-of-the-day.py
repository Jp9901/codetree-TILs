m1, d1, m2, d2 = map(int,input().split())
d1_day=input()

day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat','Sun']
num_of_days = [0,31,29,31,30,31,30,31,31,30,31,30,31]

elapsed_day = 0

if m1 == m2:
    elapsed_day = d2-d1
else:
    elapsed_day = (sum(num_of_days[m1:m2])-d1)+d2


print((elapsed_day+day.index(d1_day))//7)