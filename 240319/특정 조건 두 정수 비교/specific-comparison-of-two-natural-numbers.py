s=input()
a=int(s.split()[0])
b=int(s.split()[1])

if a<b:
    k=1
else:
    k=0

if a==b:
    j=1
else:
    j=0


print(f"{k} {j}")