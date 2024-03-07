string = list(input())

for ele in string:

    if ele.islower():
        print(ele.upper(), end ="")
    else:
        print(ele.lower(), end ="")