class info:
    def __init__(self, name, address, area):
        self.name = name
        self.address = address
        self.area = area
    
n = int(input())

# n명의 자료에 대한 리스트
info_li = list()

# 자료 입력받기
for _ in range(n):
    name, address, area = input().split()
    
    info_li.append(info(name,address,area))

min_idx = 0
# 이름이 가장 느린 사람
for i in range(n):
    if info_li[min_idx].name < info_li[i].name:
        min_idx = i

print(f"name {info_li[min_idx].name}")
print(f"addr {info_li[min_idx].address}")
print(f"city {info_li[min_idx].area}")