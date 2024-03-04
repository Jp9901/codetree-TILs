n = int(input())

for i in range(n,0,-1):
    for j in range(1,i+1):
        print(f"{n+1-i} * {j} = {(n+1-i)*j}",end="")
        if j != i:
            print(" / ", end="")
    print()