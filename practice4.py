IPs = ['192.12.14.5', '192.12.14.6', '192.12.14.8', '192.12.14.9', '192.12.14.10', '192.12.14.11', '192.12.14.13', '192.12.14.14']

broken_pc = input("Номер сломанного ПК ")

for ip in IPs:
    if broken_pc == ip.split('.')[3]:
        IPs.pop(IPs.index(ip))
print(IPs)