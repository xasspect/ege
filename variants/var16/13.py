from ipaddress import *

s = ['11111111', '11111111', '11111000']

for x in range(33):
    net = ip_network(f'118.193.30.139/{x}', 0)
    print(net)
print(int('11111000', 2))
