from ipaddress import *

for x in range(33):
    net = ip_network(f'168.224.22.193/{x}', 0)
    if str(net.network_address) == '168.224.16.0':
        print(net.netmask)
print(bin(240))