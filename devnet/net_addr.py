from netaddr import *
import pprint

ip = IPAddress('192.0.2.1')
print(ip.bits())

netmask = IPAddress('255.255.255.0')
print(netmask.bits())

ip = IPNetwork('192.0.2.0/24')
#ip.ip
#ip.network, ip.broadcast
#ip.netmask
#ip.size

print(ip.ip.bits())
print(ip.network.bits())
print(ip.netmask.bits())
print(ip.broadcast.bits())
