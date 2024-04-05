s=input()
a=int(s.split()[0])
b=int(s.split()[1])
n=input()



k=int(n,a)

#k를 b진수로 변환하자
digit=[]

while True:
    if k<b:
        digit.append(k)
        break
        
    digit.append(k%b)
    k=k//b

for d in digit[::-1]:
    print(d,end="")