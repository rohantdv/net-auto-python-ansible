# from netmiko import ConnectHandler
# from getpass import getpass
#
# # List of IP addresses for multiple Cisco devices
# multidevice333 = ["192.168.195.204", "192.168.195.205", "192.168.195.206"]
#
# # Iterate over each device in the list
# for singledevice333 in multidevice333:
#     # Connection details for each device
#     ciscodevices333 = {
#         "device_type": "cisco_ios",  # Device type (Cisco IOS)
#         "ip": singledevice333,  # IP address of the device
#         "username": getpass("Enter the username for " + singledevice333 + ": "),  # Prompt for username
#         "password": getpass("Enter the password for " + singledevice333 + ": "),  # Prompt for password
#     }
#
#     # Establish SSH connection to the device
#     ssh333 = ConnectHandler(**ciscodevices333)
#
#     # Print connection status
#     print("#" * 25)
#     print("Connecting to " + singledevice333)
#
#     # List of commands to execute on the device
#     clilist333 = ["show ip int br", "show ver", "show clock"]
#
#     # Iterate over each command and execute it on the device
#     for singlecli333 in clilist333:
#         print(">" * 5 + "Output for " + singlecli333)
#         output333 = ssh333.send_command(singlecli333)  # Execute command
#         print(output333)  # Print command output
#
#     # Disconnect from the device
#     ssh333.disconnect()
#
#     # Print disconnection status
#     print("Disconnected from " + singledevice333)
#     print("#" * 25)



# from netmiko import ConnectHandler
# from getpass import getpass
#
# # Prompting for username and password input
# user333 = getpass("Enter the username for all devices: ")  # Prompt for username
# pass333 = getpass("Enter the password for all devices: ")  # Prompt for password
#
# # List of devices to connect to
# multidevice333 = ["192.168.195.204", "192.168.195.205", "192.168.195.206"]
#
# # Iterate over each device in the list
# for singledevice333 in multidevice333:
#     # Device connection details
#     ciscodevices333 = {
#         "device_type": "cisco_ios",  # Device type
#         "ip": singledevice333,  # IP address of the device
#         "username": user333,  # Username for device
#         "password": pass333,  # Password for device
#     }
#
#     # Establish SSH connection to the device
#     ssh333 = ConnectHandler(**ciscodevices333)
#
#     # Print connection status
#     print("#" * 25)
#     print("Connecting to " + singledevice333)
#
#     # List of commands to execute on the device
#     clilist333 = ["show ip int br", "show ver", "show clock"]
#
#     # Iterate over each command and execute it on the device
#     for singlecli333 in clilist333:
#         print(">" * 5 + "Output for " + singlecli333)
#         output333 = ssh333.send_command(singlecli333)
#         print(output333)
#
#     # Disconnect from the device
#     ssh333.disconnect()
#     print("Disconnected from " + singledevice333)
#     print("#" * 25)





from netmiko import ConnectHandler
from getpass import getpass

# Prompting for username and password input
user333 = getpass("Enter the username for all devices: ")  # Prompt for username
pass333 = getpass("Enter the password for all devices: ")  # Prompt for password

# List of devices to connect to
multidevice333 = ["192.168.195.204", "192.168.195.205", "192.168.195.206"]

# Iterate over each device in the list
for singledevice333 in multidevice333:
    # Device connection details
    ciscodevices333 = {
        "device_type": "cisco_ios",  # Device type
        "ip": singledevice333,  # IP address of the device
        "username": user333,  # Username for device
        "password": pass333,  # Password for device
    }

    # Establish SSH connection to the device
    ssh333 = ConnectHandler(**ciscodevices333)

    # Print connection status
    print("#" * 25)
    print("Connecting to " + singledevice333)

    # List of commands to execute on the device
    clilist333 = ["show ip int br", "show ver", "show clock"]

    # Iterate over each command and execute it on the device
    for singlecli333 in clilist333:
        print(">" * 5 + "Output for " + singlecli333)
        output333 = ssh333.send_command(singlecli333)
        print(output333)

    # Disconnect from the device
    ssh333.disconnect()
    print("Disconnected from " + singledevice333)
    print("#" * 25)