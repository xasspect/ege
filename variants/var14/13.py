from ipaddress import *

for x in range(33):
    net = ip_network(f'115.12.69.38/{x}', 0)
    print(net)