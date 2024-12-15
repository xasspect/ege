a = list(open('24.txt'))[0]

s = ['C', 'D', 'F']
g = ['A', 'O']
t = []
for i in range(len(a) - 1):
    k = 0
    if a[i] in s and a[i + 1] in g:
        
        k += 1
    print(k)
    t.append(k)