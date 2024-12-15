a = str(open('24.txt').readlines())
o = []
t = []

for i in range(len(a) - 2):
    if (a[i:i + 2] == '+*' or a[i:i + 2] == '*+' or a[i:i + 2] == '**' or a[i:i + 2] == '++'):
        o.append(i)



for x in range(len(o) - 1):

    t.append(len(a[o[x]:o[x + 1]]))
print(max(t))

