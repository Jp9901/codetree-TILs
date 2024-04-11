#문자열 리스트에 넣고, 다음에오는 기호가 - 이면 1, +또는*이면 4로 치환하자. 
#계산하는 함수를 정의하자

def cal(a,b):   # a계산된 값(정수형), b는 리스트의 일부(문자형)
    k=int(b[-1])
    if b[0]=='+':
        return a+k
    elif b[0]=='-':
        return a-k
    else:
        return a*k


target=[i for i in input()]
n=len(target)
target[0]='4'

for i in range(2,n,2):
    if target[i-1]=='-':
        target[i]=1
    else:
        target[i]=4

    
value=4
for i in range(1,n,2):
    k=cal(value,target[i:i+2])
    value=k
    
print(value)