from ipaddress import *
k = 0
net = ip_network('235.53.0.0/255.255.224.0', 0)
for ip in net:
    s = bin(int(ip))[2:].zfill(32)
    if s.count('1') % 5 == 0:
        if s[-3:] == '110':
            print(s)
            k += 1
print(k)
