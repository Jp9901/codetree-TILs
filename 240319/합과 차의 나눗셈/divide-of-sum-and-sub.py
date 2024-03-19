string=input()

a=int(string.split()[0])
b=int(string.split()[1])

k=(a+b)/(a-b)
k=round(k,2)
print("{:.2f}".format(k))