k = 0
for list in open('910.txt').readlines():
    a = [int(x) for x in list.split()]
    a.sort()
    even = [x for x in a if x % 2 == 0]
    odd = [x for x in a if x % 2 == 1]
    if len(even) == 2 and len(odd) == 2:
        if sum(even) == sum(odd):
            k += 1

print(k)