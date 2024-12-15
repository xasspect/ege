from itertools import *
k = 0
a = product('012345', repeat=6)
for x in a:
    s = ''.join(x)

    if s[0] != '0':
        if s.count('2') == 1:
            for i in range(len(s)):
                if s[i] == s[0] and s[0] == '2':
                    if int(s[i + 1]) % 2 == 0:
                        k += 1

                elif s[i] == s[-1] and s[-1] == '2':
                    if int(s[i - 1]) % 2 == 0:
                        k += 1

                elif s[i] == '2' and s[i] != s[0] and s[i] != s[-1]:
                    if int(s[i + 1]) % 2 == 0:
                        if int(s[i-1]) % 2 == 0:
                            k += 1
print(k)