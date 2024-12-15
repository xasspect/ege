from ipaddress import *
net = ip_network('115.192.0.0/255.192.0.0', 0)
k = 0
for ip in net:
    s = bin(int(ip))[2:].zfill(32)
    if str(s).count('1') % 3 != 0:
        k += 1
print(k)