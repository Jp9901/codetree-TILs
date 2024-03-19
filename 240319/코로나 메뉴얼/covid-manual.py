def check(x,y,a):
    if x=="Y" and y>=37:
        a+=1
    return a


A=input().split()
a1=A[0]
a2=int(A[1])

B=input().split()
b1=B[0]
b2=int(B[1])

C=input().split()
c1=C[0]
c2=int(C[1])


a=0
a=check(a1,a2,a)
a=check(b1,b2,a)
a=check(c1,c2,a)

if a>=2:
    print("E")
else:
    print("N")