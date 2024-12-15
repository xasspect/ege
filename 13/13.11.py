from ipaddress import *
k = 0
net = ip_network('112.208.0.0/255.255.128.0', 0)
for ip in net:
    s = bin(int(ip))[2:].zfill(32)
    if s.count('1') % 11 == 0:
        k += 1
print(k)