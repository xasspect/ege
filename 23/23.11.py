a = []
for d in range(1, 100):
    def f(s, end, d):
        if s > end: return 0
        if s == end: return 1
        return f(s + d, end, d) + f(s * 2, end, d)
    a.append(f(1, 10, d) * f(10, 100, d))

print(a)

for i in range(len(a) - 1):
    if a[i] == 13:
        print(i + 1)