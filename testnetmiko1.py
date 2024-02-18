from netmiko import ConnectHandler

Device_list = {
    # 'device_type': 'cisco_ios',
    # 'host': '192.168.195.193',
    # 'username': 'admin',
    # 'password': 'cisco',

    'device_type': 'cisco_ios',
    'host': '192.168.195.194',
    'username': 'admin',
    'password': 'cisco',
}
net_connect = ConnectHandler(**Device_list)
output = net_connect.send_command('show ip int brief')
print(output)