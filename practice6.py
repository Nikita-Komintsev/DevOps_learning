import ipaddress
import socket


class IpAddress:
    ip_address = ''
    mask = ''
    network = ''

    def __init__(self, ip_address, ip_mask, network = None):
        self.ip_address = ip_address
        self.ip_mask = ip_mask
        self.network = str(network)

    def check(self):
        try:
            socket.inet_aton(self.ip_address)
        except socket.error:
            print('not valid ip ', self.ip_address)
        try:
            socket.inet_aton(self.ip_mask)
        except socket.error:
            print('not valid mask ', self.ip_mask)

    def network_address(self):
        network = ipaddress.IPv4Network(self.ip_address + '/' + self.ip_mask, strict=False)
        print('network_address: ', network.network_address)
        return network.network_address

    def network_to_binary(self):
        print('in binary: '+'.'.join([bin(int(x)+256)[3:] for x in self.network.split('.')]))

    def print_all(self):
        print(vars(self))


if __name__ == "__main__":
    ip = input('ip ')
    mask = input('mask ')

    IpAddress(ip, mask).check()
    network = IpAddress(ip, mask).network_address()
    IpAddress(ip, mask, network).network_to_binary()
    IpAddress(ip, mask, network).print_all()