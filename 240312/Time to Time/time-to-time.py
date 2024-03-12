hour,mins,obj_hour,obj_mins = map(int,input().split())
elapsed_t = 0

while True:
    elapsed_t += 1
    mins += 1

    if hour == obj_hour and mins == obj_mins:
        break
    
    if mins == 60:
        hour += 1
        mins = 0

print(elapsed_t)