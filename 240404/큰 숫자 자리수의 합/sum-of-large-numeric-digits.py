a,b,c=tuple(map(int,input().split()))

x=a*b*c
xs=str(x)
digits = [int(digit) for digit in xs]

print(sum(digits))