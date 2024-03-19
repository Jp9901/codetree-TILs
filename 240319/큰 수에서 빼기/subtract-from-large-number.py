s=input()

a=int(s.split()[0])
b=int(s.split()[1])

if a>=b:
    print(a-b)
else:
    print(b-a)