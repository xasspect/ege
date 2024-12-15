from random import *
x = '3'
a = ['4', '2']
for i in range(41):
    x += a[0]
for q in range(26):
    p = randint(1, len(x) - 1)
    x[p] + a[1]
x += '3'
print(x)

# while '3' in x:
#     if '342' in x:
#         x = x.replace('342', '4123', 1)
#     elif '34' in x:
#         x = x.replace('34', '413', 1)
#     elif '32' in x:
#         x = x.replace('32', '13', 1)
#     elif '33' in x:
#         x = x.replace('33', '424', 1)
# print(sum(map(int, x)))
