n=int(input())



while n<=100:
    if n<60:
        print("F",end=" ")
        n+=1
    elif n<70:
        print("D",end=" ")
        n+=1
    elif n<80:
        print("C",end=" ")
        n+=1
    elif n<90:
        print("B",end=" ")
        n+=1
    elif n<=100:
        print("A",end=" ")
        n+=1