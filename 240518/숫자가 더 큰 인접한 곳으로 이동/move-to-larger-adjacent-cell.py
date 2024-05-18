n,r,c = tuple(map(int,input().split()))
arr= [
    list(map(int,input().split()))
    for _ in range(n)
]

x, y = c-1, r-1
val = [arr[y][x]]

next_x = [0,0,-1,1]
next_y = [-1,1,0,0]

# 큰 값이 존재하는지
def check_max(x,y):
    for dx,dy in zip(next_x,next_y):
        x2,y2 = x+dx, y+dy

        if x2 < 1 or x2 > n or y2 < 0 or y2 > n:
            continue 

        if arr[y][x] < arr[y2][x2]:
            return True
    return False

while check_max(x,y):
    for dx,dy in zip(next_x,next_y):
        x2,y2 = x+dx, y+dy
        if x2 < 1 or x2 > n or y2 < 0 or y2 > n:
            continue

        if arr[y][x] < arr[y2][x2]:
            val.append(arr[y2][x2])
            x,y = x2,y2

print(*val)