b = list(range(34, 73))
c = list(range(32, 61))
a = []
for x in range(1, 150):
    if not(((x in b) <= (x in a)) and ((not(x in c)) or (x in a))):
        a.append(x)
print(72 - 32)