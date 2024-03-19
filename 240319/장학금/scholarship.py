s=input()
s=s.split()

mid=int(s[0])
fin=int(s[1])

if mid<90:
    print(0)
elif (fin<90):
    print(0)
elif (90<=fin & fin<95):
    print(5)
elif fin>=95:
    print(10)