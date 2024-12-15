from ipaddress import *

net = ip_network('112.160.0.0/255.240.0.0', 0)
s = 0
for ip in net:
    if int(f'{ip:b}') % 5 == 0:
        s += 1
print(s)