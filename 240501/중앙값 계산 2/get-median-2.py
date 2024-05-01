n = int(input())

# 입력받은 변수들의 리스트
nums_input = list(map(int,input().split()))

# 위 리스트에서 하나씩 추가
nums_li = list()
for num in nums_input:
    nums_li.append(num)
    lo = len(nums_li)

    if lo%2 == 1:
        nums_li.sort()
        print(nums_li[lo//2], end=' ')