# a = list(open('24.txt'))[0]
# k = 0
# for i in range(len(a) - 6):
#     x1 = a[i]
#     x2 = a[i + 1]
#     x3 = a[i + 2]
#     x4 = a[i + 3]
#     x5 = a[i + 4]
#     x6 = a[i + 5]
#
#     if x1 != 'X' and x6 != 'X':
#         if x2 + x3 + x4 + x5 == 'XXXX':
#             print(x1,x2,x3,x4,x5,x6)
#             k += 1
# print(k)

a = list(open('24.txt'))[0]
k = 0
for i in range(len(a) - 4):
    x1 = a[i]
    x2 = a[i + 1]
    x3 = a[i + 2]
    x4 = a[i + 3]

    if x1 + x2 + x3 + x4 == 'XXXX':
        k += 1
    # if x1 != 'X' and x6 != 'X':
    #     if x2 + x3 + x4 + x5 == 'XXXX':
    #         print(x1,x2,x3,x4,x5,x6)
    #         k += 1
print(k)