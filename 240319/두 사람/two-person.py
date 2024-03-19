a=input()
age1=int(a.split()[0])
s1=a.split()[1]
b=input()
age2=int(b.split()[0])
s2=b.split()[1]


if (age1>=19 and s1=="M")or(age2>=19 and s2=="M"):
    print(1)
else:
    print(0)