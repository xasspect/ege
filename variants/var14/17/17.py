a = list(map(int, open('17.txt')))


def f2(n):
    b = ''
    while n:
        b = str(n % 2) + b
        n//= 2
    return b

def f5(n):
    b = ''
    while n:
        b = str(n % 5) + b
        n//= 5
    return b

k = 0
t = []
for i in a:
    i2 = f2(i)
    i5 = f5(i)
    if str(i2)[-1] == str(i5)[-1]:
        if i % 31 == 0 or i % 47 == 0 or i % 53 == 0:
            k +=1
            t.append(i)
print(k, min(t))