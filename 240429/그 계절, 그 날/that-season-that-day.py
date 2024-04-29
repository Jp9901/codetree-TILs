Y,M,D = map(int, input().split())

# 윤년 확인 함수
def discrim_Feb(year):
    dis = False # 윤년이면 True, 아니라면 False

    if year%4 == 0:
        dis=True
        if year%100 == 0:
            dis=False
            if year%400 == 0:
                dis = True
            
    return dis

# 날짜 존재 확인 함수
def discrim_day(year, month, day):
    dis = False # 날짜가 존재하면 True, 아니라면 False
    
    # 1~31일
    if month in [1,3,5,7,8,10,12]:
        if day <= 31:
            dis = True
    
    # 2월 1~28일/ 29일(윤년)
    elif month == 2:
        if discrim_Feb(year):
            if day <= 29:
                dis = True
        else:
            if day <= 28:
                dis = True

    # 1~30일
    else:
        if day <= 30:
            dis = True

    return dis

if discrim_day(Y,M,D):
    if M in [12,1,2]:
        print('Winter')
    elif M in [3,4,5]:
        print('Spring')
    elif M in [6,7,8]:
        print('Summer')
    else:
        print('Fall')
else:
    print(-1)