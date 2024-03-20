k=int(input())
s=0
a=0
for _ in range(k):
    n=int(input())
    s+=n
    a+=1

m=round(s/a,1)
print(s,end=" ")
print(m)