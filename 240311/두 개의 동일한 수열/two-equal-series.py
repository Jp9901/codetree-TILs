n = int(input())

A = list(map(int, input().split())).sort()
B = list(map(int, input().split())).sort()

if A == B:
    print("Yes")
else:
    print("No")