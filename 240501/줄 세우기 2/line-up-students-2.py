class Student:
    def __init__(self, h, w, idx):
        self.h = h
        self.w = w
        self.idx = idx

n = int(input())

Students=list()

for i in range(n):
    h,w = map(int, input().split())
    Students.append(Student(h,w,i))

Students.sort(key=lambda x: (x.h, -x.w))

for stu in Students:
    print(stu.h, stu.w, stu.idx+1)