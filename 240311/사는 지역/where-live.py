class information:
    def __init__(self, name, str_num, address):
        self.name = name
        self.str_num = str_num
        self.address = address
    

n = int(input())
informs = []

for _ in range(n):
    name, str_num, address = map(tuple, input().split(' '))
    informs.append(information("".join(name),"".join(str_num),"".join(address)))

last_idx = 0
last_name = informs[last_idx].name
for i in range(1,n):
    if last_name < informs[i].name:
        last_name = informs[i].name
        last_idx = i


print(f"""name {informs[i].name}
addr {informs[i].str_num}
city {informs[i].address}""")