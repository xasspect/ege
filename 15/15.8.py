M = [x for x in range(32, 69)]
N = [x for x in range(54, 77)]
a = []
for x in range(1, 101):
    if (not(((x in M) or (x in N)) == (not(x in a)))):
        a.append(x)
print(76 - 32)