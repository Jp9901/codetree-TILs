def season(Y,M,D):
    if M== (1 or 3 or 5 or 7 or 8 or 10 or 12):
        if D >31:
            return -1
        if M==3 or 5:
            return 'Spring'
        elif M == 7 or 8:
            return "Summer"
        elif M==10:
            return "Fall"
        else:
            return "Winter"
    
    elif M== (4 or 6 or 9 or 11):
        if D >30:
            return -1
        if M==4:
            return 'Spring'
        elif M == 6:
            return "Summer"
        elif M==9:
            return "Fall"
        else:
            return "Winter"
    
    else:
        if Y%4 == 0  and Y%100 == 0 and Y%400 ==0:
            if D > 29:
                return -1
            return "Winter"
        else:
            if D>28:
                return -1
            return "Winter"


Y, M, D = map(int,input().split())

print(season(Y,M,D))