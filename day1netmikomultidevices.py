"""
This script connects to multiple Cisco IOS devices using SSH and retrieves various pieces of information.
It iterates over a list of device IP addresses, establishes an SSH connection to each device,
executes a set of predefined CLI commands, and prints the output of each command.

Note: Ensure that the netmiko library is installed before running this script.
"""

from netmiko import ConnectHandler

# Define a list of device IP addresses
multiple_device_ips = ["192.168.195.201", "192.168.195.202", "192.168.195.203"]

# Iterate over each device IP address
for single_device_ip in multiple_device_ips:
    # Define device information dictionary for Cisco IOS devices
    cisco_device_info = {
        "device_type": "cisco_ios",
        "ip": single_device_ip,
        "username": "admin",
        "password": "cisco",  # Ensure the correct password is provided
    }

    # Establish SSH connection to the device
    ssh_connection = ConnectHandler(**cisco_device_info)

    # Print separator line for clarity
    print("#" * 25)
    # Print status message indicating connection to the current device
    print("Connecting to " + single_device_ip)

    # Define a list of CLI commands to execute on the device
    cli_commands = ["show ip int br", "show ver", "show clock"]

    # Iterate over each CLI command
    for cli_command in cli_commands:
        # Print separator for each command's output
        print(">" * 5 + " Output for " + cli_command)
        # Send the command over the SSH connection and receive output
        command_output = ssh_connection.send_command(cli_command)
        # Print the output of the command
        print(command_output)

    # Print status message indicating disconnection from the current device
    print("Disconnected from " + single_device_ip)
    # Print separator line for clarity
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
#     clilist123 = ["show ip int br", "show ver", "show clock"]
#     for singlecli123 in clilist123:
#         print(">"* 5 + "Output for " + singlecli123)
#         output123 = ssh123.send_command(singlecli123) #write over trasnport channel
#         print(output123)
#     print("Disconnected from " + singledevice123)
#     print("#" * 25)

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

