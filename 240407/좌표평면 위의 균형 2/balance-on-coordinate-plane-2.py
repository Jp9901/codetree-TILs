#2부터 100까지의 모든 (짝수,짝수) 좌표들을 탐색
#각 좌표마다 네구역의 점의 개수를 카운트 (리스트 [,,,]에 넣자)
#리스트의 최대값을 갱신하면서 진행하자. 

N=int(input())

points=[tuple(map(int,input().split())) for _ in range(N)]

value=N


for i in range(50):
    for j in range(50):
        a,b=2*i,2*j
        count=[0]*4

        for x,y in points:
            if x>a and y>b:
                count[0]+=1
            elif x<a and y>b:
                count[1]+=1
            elif x<a and y<b:
                count[2]+=1
            else:
                count[3]+=1
        
        value=min(max(count),value)


print(value)