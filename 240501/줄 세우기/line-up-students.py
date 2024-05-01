class Student:
    def __init__(self,h,w,idx):
        self.h=h
        self.w=w
        self.idx=idx

n = int(input())

students = list()
for i in range(1,n+1):
    h, w = map(int, input().split())
    students.append(Student(h,w,i))

students.sort(key=lambda x : (-x.h, -x.w, x.idx))

for i in range(n):
    print(students[i].h, students[i].w, students[i].idx)