from ipaddress import *



for m in range(0, 33):



    net = ip_network(f'117.184.113.45/{m}', 0)

    if str(net.network_address) == '117.184.64.0':
        print(net.netmask)

