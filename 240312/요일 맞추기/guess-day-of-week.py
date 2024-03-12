m1, d1, m2, d2 = tuple(map(int,input().split()))

month = [0,31,28,31,30,31,30,31,31,30,31,30,31]
day = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
elapsed_d = (month[m2]+d2) - (month[m1]+d1)

pos = abs(elapsed_d)%7
if elapsed_d < 0:
    print(day[-pos])
else:
    print(day[pos])