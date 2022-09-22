import wmi


def getAdapterInfo():
    nics = []
    nic_configs = wmi.WMI().Win32_NetworkAdapterConfiguration(IPEnabled=1)
    for interface in nic_configs:
        # print(interface.Caption)
        # print(interface.Description)
        nic = {}
        nic['name'] = interface.Description
        nic['mac'] = interface.MACAddress
        nic['ipv4'] = {'address': [], 'gateway': []}
        nic['ipv6'] = {'address': [], 'gateway': []}
        if interface.IPAddress is not None:
            for ip_address in interface.IPAddress:
                ip = {}
                # ipv4 address
                if '.' in ip_address:
                    ip['ip'] = ip_address
                    ip['subnetmask'] = interface.IPSubnet[0]
                    nic['ipv4']['address'].append(ip)
                # ipv6 address
                elif ':' in ip_address:
                    ip['ip'] = ip_address
                    nic['ipv6']['address'].append(ip)
            

                # print(ip_address)
                # print(interface.IPEnabled)
                # print(interface.DHCPEnabled)
                # print(interface.MACAddress)
                # print(interface.IPSubnet)
                # print(interface.DefaultIPGateway)
                # print("")
            
        
        if interface.DefaultIPGateway is not None:
            for gateway in interface.DefaultIPGateway:
                gw = {}
                # ipv4 gateway
                if '.' in gateway:
                    gw['gateway'] = gateway
                    nic['ipv4']['gateway'].append(gw)
                # ipv6 gateway
                elif ':' in gateway:
                    gw['gateway'] = gateway
                    nic['ipv6']['gateway'].append(gw)

        nics.append(nic)
    return nics

getAdapterInfo()