def printIf(arggg):
        addrs = psutil.net_if_addrs()
        # print(addrs.keys())

        for entry in addrs:
            print(entry)
            for value in range(0, len(addrs[entry]) -1):
                if addrs[entry][value][0] == -1:
                    print("Link")
                if addrs[entry][value][0] == 2:
                    print("IPv4")
                    print(addrs[entry][value][1])   #IP
                    print(addrs[entry][value][2])   #SN Mask
                if addrs[entry][value][0] == 23:
                    print("IPv6")
                    print(addrs[entry][value][1])   #IP
                print(" ")
            print("======================================")