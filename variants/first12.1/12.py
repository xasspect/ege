for n in range(1, 100):
    s = '3' * 15 + '2' * 18 + '1' * n

    while '31' in s or '33' in s or '21' in s:
        if '31' in s:
            s = s.replace('31', '123', 1)

        if '33' in s:
            s = s.replace('33', '211', 1)
        if '21' in s:
            s = s.replace('21', '1', 1)
    if sum(map(int, s)) > 24:
        print(n)



