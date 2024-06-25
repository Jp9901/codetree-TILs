#5로 나눈 몫만큼 반복

#1. 5동전 다 쓰고 남은 수가 2로 나누어 떨어질때
#2. 2로 나누어 떨어지지 않으면 continue
#3. i가 0이고 2로 떨어지지 않으면 -1 
n=int(input())


five=n//5



for i in range(five,-1,-1):
    m=n-(i*5)
    two=m//2
    if m%2==0:
        print(i+two)
        break
    elif m%2!=0 and i!=0:
        continue
    elif m%2!=0 and i==0:
        print(-1)
        break