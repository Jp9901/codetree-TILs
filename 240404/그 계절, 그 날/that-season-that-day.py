Y,M,D= tuple(map(int,input().split())) 

def check_y(Y):
    if Y%400==0:
        return True
    elif Y%4==0 and Y%100==0:
        return False

    elif Y%4==0:
        return True
    else:
        return False


def check(Y,M,D):
    list_30=[4,6,9,11]
    

    if (M in list_30)and M>30:
        return True
    elif  (M==2)and check_y and M>29:
        return True

    elif  (M==2)and M>28:
        return True
    else:
        return False

    

def solution(Y,M,D):
    if check(Y,M,D):
        print(-1)
    elif 2<M and M<6:
        print("Spring")
    elif 5<M and M<9:
        print("Summer")
    elif 8<M and M<12:
        print("Fall")
    else:
        print("Winter")




solution(Y,M,D)