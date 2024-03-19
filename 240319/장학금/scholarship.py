s=input()
s=s.split()

mid=int(s[0])
fin=int(s[1])

if mid<90:
    print(0)
elif mid>=90 & (fin<90):
    print(0)
elif mid>=90 & (90<=fin & fin<95):
    print(5)
elif mid>=90 & fin>=95:
    print(10)