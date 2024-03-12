a, b = tuple(map(int, input().split()))
n = input()

digits_10 = 0
digits_b = []
for i in range(len(n)):
    digits_10 = digits_10 * a + int(n[i])

while digits_10 > 0:
    digits_b.insert(0,digits_10%b)
    digits_10 //= b

for ele in digits_b:
   print(ele, end="")