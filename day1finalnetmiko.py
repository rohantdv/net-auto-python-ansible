from netmiko import ConnectHandler

# List of IP addresses of multiple devices
multidevice33 = ["192.168.195.201", "192.168.195.202", "192.168.195.203"]

# Loop through each device IP address
for singledevice33 in multidevice33:
    # Device connection information
    ciscodeviceinfo33 = {
        "device_type": "cisco_ios",
        "ip": singledevice33,  # Use the current device IP from the loop
        "username": "admin",
        "password": "cisco",
    }

    # Establish SSH connection to the device
    ssh123 = ConnectHandler(**ciscodeviceinfo33)

    # Print separator for readability
    print("#" * 25)

    # Print status message indicating connection to the current device
    print("Connecting to " + singledevice33)  # Use the current device IP from the loop

    # List of CLI commands to execute on the device
    clilist123 = ["show ip int br", "show ver", "show clock"]

    # Loop through each CLI command
    for singlecli123 in clilist123:
        # Print header for the output of each command
        print(">" * 5 + "Output for " + singlecli123)

        # Send the CLI command and capture the output
        output123 = ssh123.send_command(singlecli123)  # Write over transport channel

        # Print the output of the command
        print(output123)

    # Disconnect from the device after executing commands
    ssh123.disconnect()

    # Print status message indicating disconnection from the current device
    print("Disconnected from " + singledevice33)  # Use the current device IP from the loop

    # Print separator for readability
    print("#" * 25)
