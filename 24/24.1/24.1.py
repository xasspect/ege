count_y = 0

a = str(open('24.txt').readlines())
obj = []
fd = []

for i in range(len(a) - 1):
    if a[i] == 'X':
        fd.append(i)

for x in range(len(fd) - 1):
    obj.append(fd[x + 1] - fd[x] - 2)
print(max(obj))






