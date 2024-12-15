def f(n):
    b = ''
    while n:
        b = str(n % 3) + b
        n //= 3
    return b

def sm(el):
    return sum(int(c) for c in el)

res = []
for n in range(1, 100000):
    s = f(n)
    if sm(s) % 4 == 0:
        s = '1' + s
        s = s[:-2]
    else:
        s += f(sm(s) % 4 * 3)
    r = int(s, 3)
    if r > 353:
        res += [r]
print(min(res))

# def tr(x):
#     b = ''
#     while x:
#         b = str(x % 3) + b
#         x //= 3
#     return b
#
# def sm(el):
#     return sum(int(c) for c in el)
#
# res = []
# for n in range(1, 100000):
#     b = tr(n)
#     if sm(b) % 4 == 0:
#         b = '1' + b
#         b = b[:-2]
#     else:
#         b += tr( sm(b) % 4 * 3 )
#     r = int(b, 3)
#     print(r)
#     if r > 353:
#         res += [r]
# print(min(res))

