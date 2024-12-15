from ipaddress import *

for x in range(1,32):

    net = ip_network(f'111.24.160.159/{x}', 0)
    if str(net.network_address) == '111.24.160.128':
        print(x)