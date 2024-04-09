#뒷자리부터 채우자. 
#리스트 받아서 정렬하고, 뒷자리로 옮긴다.   


#뒷자리로 옮기는데 필요한 값을 계산하는 함수 check를 정의한다 
#가장 큰수부터 check하고 cnt에 갱신하고, 큰수 지우고, 맨뒤에 넣는다

import string                    

a_to_num = {letter: i for i, letter in enumerate(string.ascii_uppercase,start=1)}

def check(numbers,k):
    g=index.index(k)
    h=numbers.index(k)
    return g-h



n=int(input())
a=list(input().split())
numbers=[]                 #[1,4,3,2]
for i in range(n):
    numbers.append(a_to_num[a[i]]) 


index=sorted(numbers)       #[1,2,3,4]

cnt=0
for i in index[::-1]:
    t=numbers.index(i)     
    z=check(numbers,i)                       
    cnt+=z
    numbers=list(set(numbers)-set([i]))    
    numbers=numbers[0:t+z]+[i]+numbers[t+z:-1]




print(cnt)