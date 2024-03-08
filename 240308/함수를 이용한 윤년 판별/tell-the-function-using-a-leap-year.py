def dis(y):
    if y%4 == 0:
        if y%100 ==0 and y%400 != 0:
            return 'false'
        return "true"
    else:
        return 'false'

year = int(input())

print(dis(year))