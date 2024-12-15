from ipaddress import *
k = 0
net = ip_network('214.187.224.0/255.255.224.0', 0)

for ip in net:
    s = bin(int(ip))[2:].zfill(32)
    if s.count('1') % 6 != 0:
        if s[-4:] == '1000':
            print(s)
            k += 1
print(k)
