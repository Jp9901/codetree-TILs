string = input()

n = 0
for i in range(len(string)):
    if string[i] == 'e':
        n += 1
    
    if n == 1:
        n = 100
        continue
    print(string[i], end ='')