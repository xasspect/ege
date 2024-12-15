def f(n):
    b = ''
    while n:
        b = str(n % 2) + b
        n //= 2
    return b


for n in range(1, 100):
    s = f(n)

    if s.count('0') == s.count('0'):
        s += s[-1]
    elif s.count('0') > s.count('1'):
        s += '1'
    elif s.count('0') < s.count('1'):
        s += '0'
    if s.count('0') == s.count('0'):
        s += s[-1]
    elif s.count('0') > s.count('1'):
        s += '1'
    elif s.count('0') < s.count('1'):
        s += '0'
    # if s.count('0') == s.count('0'):
    #     s += s[-1]
    # elif s.count('0') > s.count('1'):
    #     s += '1'
    # elif s.count('0') < s.count('1'):
    #     s += '0'
    # if s.count('0') == s.count('0'):
    #     s += s[-1]
    # elif s.count('0') > s.count('1'):
    #     s += '1'
    # elif s.count('0') < s.count('1'):
    #     s += '0'
    # print(s)
    r = int(s, 2)
    # print(r)
    if r % 4 == 0 and r % 8 != 0:
        print(n)

