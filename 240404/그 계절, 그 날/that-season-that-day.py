Y,M,D= tuple(map(int,input().split())) 

def check_y(Y):
    if Y % 400 == 0:
        return True
    elif Y % 100 == 0:
        return False
    elif Y % 4 == 0:
        return True
    else:
        return False


def check(Y,M,D):
    list_30=[4,6,9,11]
    
    if (M in list_30)and D>30:
        return True
    elif  (M==2)and check_y(Y) and D>29:
        return True

    elif  (M==2)and D>28 and (not check_y(Y)):
        return True
    elif D>31:
        return True

    else:
        return False

    

def solution(Y, M, D):
    if check(Y, M, D):
        print(-1)
    elif 3 <= M <= 5:
        print("Spring")
    elif 6 <= M <= 8:
        print("Summer")
    elif 9 <= M <= 11:
        print("Fall")
    else:
        print("Winter")




solution(Y,M,D)