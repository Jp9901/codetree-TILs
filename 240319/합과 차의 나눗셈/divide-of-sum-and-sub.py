string=input()

a=int(string.split()[0])
b=int(string.split()[1])

k=(a+b)/(a-b)

print(round(k,2))