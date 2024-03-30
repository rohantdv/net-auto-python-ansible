from netmiko import ConnectHandler

multidevice33 = ["192.168.195.201", "192.168.195.202", "192.168.195.203"]

for singledevice33 in multidevice33:
    ciscodeviceinfo33 = {
        "device_type": "cisco_ios",
        "ip": singledevice33,  # Fix: Use the current device IP from the loop
        "username": "admin",
        "password": "cisco",
    }
    ssh123 = ConnectHandler(**ciscodeviceinfo33)
    print("#" * 25)
    print("Connecting to " + singledevice33)  # Fix: Use the current device IP from the loop
    clilist123 = ["show ip int br", "show ver", "show clock"]
    for singlecli123 in clilist123:
        print(">" * 5 + "Output for " + singlecli123)
        output123 = ssh123.send_command(singlecli123)  # Write over transport channel
        print(output123)
    ssh123.disconnect()  # Disconnect from the device
    print("Disconnected from " + singledevice33)  # Fix: Use the current device IP from the loop
    print("#" * 25)
