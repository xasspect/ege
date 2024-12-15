from ipaddress import *
k = 0
net = ip_network('172.16.128.0/255.255.192.0', 0)
for ip in net:
    s = bin(int(ip))[2:].zfill(32)
    if s.count('1') % 2 != 0:
        k += 1
print(k)