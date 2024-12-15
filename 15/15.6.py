b = list(range(24, 91))
c = list(range(47, 116))
a = []
for x in range(1, 101):
    if not((x in c) <= (((not(x in a)) and (x in b)) <= (not(x in c)))):
        a.append(x)
print(90 - 47)
