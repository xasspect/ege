a = [x for x in list(open('24.txt').readlines())[0]]

t = []
y = []
for i in range(len(a) - 1):

    if a[i] == 'A':
        y.append(i)
        print('A', i)


    if a[i] == 'D':
        print('D', i)
        if len(y) > 0:
            t.append(i - y[-1] + 2)
print(max(t))












print(t)





