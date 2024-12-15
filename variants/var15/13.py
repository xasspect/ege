from ipaddress import *
k = 0
net = ip_network('165.44.96.0/255.255.248.0', 0)
for ip in net:
    s = bin(int(ip))[2:].zfill(32)
    for i in range(len(s) - 2):
        x1 = s[i]
        x2 = s[i + 1]
        x3 = s[i + 2]
        if x1 + x2 + x3 == '111':
            k += 1

            break

print(k)
