
t = []
for n in range(4, 10000):
    s = '3' + '5' * n
    while '333' in s or '555' in s:
        if '555' in s:
            s = s.replace('555', '3', 1)
        else:
            s = s.replace('333', '5', 1)
    t.append(int(s))
print(max(t))