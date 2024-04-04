n=int(input())
students=[]
for i in range(n):
    a=list(map(int,input().split()))
    a.append(i+1)
    students.append(tuple(a))

students.sort(lambda x:(x[0],-x[1]))
for a,b,c in students:
    print(a,b,c)