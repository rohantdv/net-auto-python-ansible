from netmiko import ConnectHandler
ciscodevice = {
    "device_type":"cisco_ios",
    "username":"admin",
    "password":"cisco",
    "ip":"192.168.195.201",
}
ssh = ConnectHandler(**ciscodevice)
output = ssh.send_command("show ip int br")
print(output)