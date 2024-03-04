n = int(input())

for i in range(n,0,-1):
    print('*'*i,'*'*i, sep = ' '*2*(4-i))