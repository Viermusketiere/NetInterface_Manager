import wmi

nics = []



nic_configs = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=1)
for interface in nic_configs:
    print(interface.Caption)
    print(interface.Description)
    nic = {}
    nic['name'] = interface.Description
    nic['mac'] = interface.MACAddress
    nic['ipv4'] = []
    nic['ipv6'] = []
    if interface.IPAddress is not None:
        for ip_address in interface.IPAddress:
            ip = {}
            # ipv4 address
            if '.' in ip_address:
                ip['ip'] = ip_address
                ip['subnetmask'] = interface.IPSubnet
                nic['ipv4'].append(ip)
            # ipv6 address
            elif ':' in ip_address:
                ip['ip'] = ip_address
                nic['ipv6'].append(ip)
        
            


            
            print(ip_address)
            print(interface.IPEnabled)
            print(interface.DHCPEnabled)
            print(interface.MACAddress)
            print(interface.IPSubnet)
            print(interface.DefaultIPGateway)
            print("")
        nics.append(nic)

print("Done")