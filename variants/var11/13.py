from ipaddress import *

for x in range(33):
    net = ip_network(f'203.155.64.98/{x}', 0)
    print(net)