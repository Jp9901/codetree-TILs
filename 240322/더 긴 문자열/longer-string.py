string=input()
inx=string.index(" ")

a=string[:inx]
b=string[inx+1:]

if len(a)==len(b):
    print("same")
elif len(a)>len(b):
    print(a, end=" ")
    print(len(a))
else:
    print(b, end=" ")
    print(len(b))