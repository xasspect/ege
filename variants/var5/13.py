from ipaddress import *

for x in range(16, 25):
    net = ip_network(f'246.51.128.202/{16}', 0)
    for ip in net:
        if f'{ip:b}'[:16].count('0') <= f'{ip:b}'[16:].count('0'):
            print(x)
