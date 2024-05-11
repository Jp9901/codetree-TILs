# 명령어 종류
def command(com_type):
    com = com_type[0]
    if com == 'push_back':
        n = int(com_type[1])
        li.append(n)
    elif com == 'pop_back':
        li.pop()
    elif com == 'size':
        print(len(li))
    elif com == 'get':
        n = int(com_type[1])
        print(li[n-1])

n = int(input())
li =[]

for _ in range(n):
    com = input().split()
    command(com)