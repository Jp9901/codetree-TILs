def season(Y,M,D):
    if M==1 or M==3 or M==5 or M==7 or M==8 or M==10 or M==12:

        if D >31:
            return -1
        if M==3 or M==5:
            return 'Spring'
        elif M == 7 or M==8:
            return "Summer"
        elif M==10:
            return "Fall"
        else:
            return "Winter"
    
    elif M==4 or M==6 or M==9 or M==11:

        if D >30:
            return -1
        if M==4:
            return 'Spring'
        elif M == 6:
            return "Summer"
        else:
            return "Fall"
    
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