n = int(input())
arr =[
    input().split() for _ in range(n)   
]

sum_val = 0
for i in range(n):
    sum_val += int(arr[i][0])

tile = [0 for _ in range(2*sum_val+1)]
pos = sum_val

for i in range(n):
    x = int(arr[i][0])
    if arr[i][1] == 'R':
        tile[pos:(pos+x+1)] = [-1 for _ in range(x)] # black
        pos = pos + (x-1)
    else:
        tile[pos: (pos-x):-1] = [1 for _ in range(x)] # white
        pos = pos - (x-1)

cnt_wh = tile.count(1)
cnt_bl = tile.count(-1)
print(cnt_wh,cnt_bl, sep = " " )