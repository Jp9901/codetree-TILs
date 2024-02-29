a = int(input())
b,c,d,e = map(int, input().split())

for i in b,c,d,e:
    print(1 if a>i else 0)