b = [x for x in range(34, 73)]
c = [x for x in range(32, 62)]
a = []
for x in range(1, 100):
    if not(((x in b) <= (x in a)) and ((not(x) in c) or (x in a))):
        a.append(x)
print(72 - 32)