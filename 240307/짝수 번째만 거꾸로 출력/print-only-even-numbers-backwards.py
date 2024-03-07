string = input()

arr=list()
for i in range(len(string)):
    if i%2 == 1:
        arr.append(string[i])

for ele in arr[::-1]:
    print(ele,end="")