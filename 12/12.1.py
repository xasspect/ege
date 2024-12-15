x = ''
for i in range(1, 135):
    x += '9'

while '22222' in x or '9999' in x:
    if '22222' in x:
        x = x.replace('22222', '99', 1)
    else:
        x = x.replace('9999', '2', 1)
print(x)