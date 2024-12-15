P = [x for x in range(15, 41)]
Q = [x for x in range(21, 64)]
a = []
for x in range(1, 1000):
    if not((x in P) <= (((x in Q) and (not(x in a))) <= (not(x in P)))):
        a.append(x)
print(40 - 21)

