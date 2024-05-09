n = int(input())
num = list(map(int,input().split()))
num.sort(reverse=True)

a,b,c = num[0:3]
x,y,z = num[-3:]

# 최댓값이 양수일 때,
if a*b*c > 0 or a*y*z > 0:
    val = max(a*b*c,a*y*z)

# 최대값이 음수일 때,
elif a*b*c <0 or a*y*z < 0:
    val = max(a*b*c,a*y*z)

# 최댓값이 0일 때,
else:
    val = 0


print(val)



# # 양수 3개
# if num[0]>0 and num[1]>0 and num[2]>0:
#     val1 = num[0]*num[1]*num[2]
# # 양수 1개 + 음수 2개
# if num[0]>0 and num[-1]<0 and num[2]<0:
#     val2 = num[0]*num[1]*num[2]
# max_val = max(val1,val2)