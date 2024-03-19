A=input().split()
a1=A[0]
a2=int(A[1])

B=input().split()
b1=A[0]
b2=int(A[1])

C=input().split()
c1=A[0]
c2=int(A[1])

a=0
if a1=="Y" and a2>=37:
    a+=1

if b1=="Y" and b2>=37:
    a+=1

if c1=="Y" and c2>=37:
    a+=1

if a>=2:
    print("E")
else:
    print("N")