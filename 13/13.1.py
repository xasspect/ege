from ipaddress import *
k = 0
net = ip_network('123.222.111.192/255.255.255.248', 0)
for ip in net:
    ip = str(ip)
    s = ip[-3:]
    if str(bin(int(s))[2:]).count('0') % 3 != 0:
        k += 1
print(k)
