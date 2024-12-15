a = '3' * 111
while '33333' in a or '1111' in a:
    if '33333' in a:
        a = a.replace('33333', '111', 1)
    else:
        a = a.replace('111', '33', 1)
s = 0
for i in a:
    s += int(i)
print(s)
