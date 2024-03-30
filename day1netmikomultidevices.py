from netmiko import ConnectHandler
multipledevice123 = ["192.168.195.201","192.168.195.202","192.168.195.203"]
for singledevice123 in multipledevice123:
    ciscodeviceinfo123 = {
        "password": "cisco",
        "ip": singledevice123,
        "username": "admin",
        "device_type": "cisco_ios",
    }
    ssh123 = ConnectHandler(**ciscodeviceinfo123)
    #ssh is etsbld
    print("#" * 25)
    print("Connecting to " + singledevice123)
    clilist123 = ["show ip int br", "show ver", "show clock"]
    for singlecli123 in clilist123:
        print(">"* 5 + "Output for " + singlecli123)
        output123 = ssh123.send_command(singlecli123) #write over trasnport channel
        print(output123)
    print("Disconnected from " + singledevice123)
    print("#" * 25)

# from netmiko import ConnectHandler
# multipledevice123 = ["192.168.195.201","192.168.195.202","192.168.195.203"]
# for singledevice123 in multipledevice123:
#     ciscodeviceinfo123 = {
#         "password": "cisco",
#         "ip": singledevice123,
#         "username": "admin",
#         "device_type": "cisco_ios",
#     }
#     ssh123 = ConnectHandler(**ciscodeviceinfo123)
#     #ssh is etsbld
#     print("#" * 25)
#     print("Connecting to " + singledevice123)
#     clilist123 = ["show ip int br", "show run", "show clock", "show ip route"]
#     for singlecli123 in clilist123:
#         print(">" * 5 + "output for " + singlecli123)
#         output123 = ssh123.send_command(singlecli123) #write over trasnport channel
#         print(output123)
#     print("Disconnected from " + singledevice123)
#     print("#" * 25)
