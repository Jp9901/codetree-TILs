m1, d1, m2, d2=tuple(map(int,input().split()))
day=input()

month_list=[0,31,29,31,30,31,30,31,31,30,31,30,31]

def how_many_day(m,d):
    a=sum(month_list[:m-1])
    b=d
    return a+b

k=how_many_day(m2,d2)-how_many_day(m1,d1)

x=k//7
#0이면 같은 요일, 1이면 다음요일... 
days=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

dayday=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun',
        'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

if day=='Mon':
    i=0
elif day=='Tue':
    i=1
elif day=='Wed':
    i=2
elif day=='Thu':
    i=3
elif day=='Fri':
    i=4
elif day=='Sat':
    i=5
else:
    i=6


print(x)