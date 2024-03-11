class student:
    def __init__(self, h,w,idx):
        self.h = h
        self.w = w
        self.idx = idx

N = int(input())

students = []
for i in range(N):
    h,w = tuple(input().split())
    students.append(student(int(h),int(w),i+1))

students.sort(key = lambda x: (x.h,-x.w))

for i in range(N):
    print(students[i].h, students[i].w ,students[i].idx, sep = " ")