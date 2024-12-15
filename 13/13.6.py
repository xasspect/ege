from ipaddress import *
k = 0
net = ip_network('211.46.0.0/255.255.128.0', 0)
for ip in net:
    s = bin(int(ip))[2:].zfill(32)
    if s.count('1') % 4 == 0:
        if s[-2:] == '11':
            k += 1
print(k)