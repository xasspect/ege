a = open('17.txt')
s = [int(x) for x in a]

mink = []
maxk = []


for x in range(len(s)):
    if x % 7 == 0:
        mink.append(x)
    elif x % 13 == 0:
        maxk.append(x)
if min(mink) < min(maxk):
    print(len(mink), max(mink))
# elif min(mink) < min(maxk):
#     print(len(maxk), max(maxk))
