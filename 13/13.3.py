from ipaddress import *

net = ip_network('228.172.236.0/255.255.240.0', 0)
k = 0
for ip in net:
    s = f'{ip:b}'
    if s.count('1') % 5 != 0:
        k += 1
print(k)