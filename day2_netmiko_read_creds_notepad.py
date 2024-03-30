# Importing necessary module
from netmiko import ConnectHandler

# Read credentials from file
with open(r"C:\Users\Rohan\Documents\devicecreds.txt", "r") as file:
    devicecreds333 = file.read().splitlines()

# Extracting username and password from the credentials file
user333 = devicecreds333[0]  # Username
pass333 = devicecreds333[1]  # Password

# Read device list from file
with open(r"C:\Users\Rohan\Documents\devicelist.txt", "r") as file:
    readdevicelist333 = file.read().splitlines()

# Check if the device list is empty
if not readdevicelist333:
    print("No devices found in devicelist.txt")
    exit()

# Iterate over devices in the list
for singledevice333 in readdevicelist333:
    # Configuration dictionary for Cisco device
    ciscodeviceinfo333 = {
        "device_type": "cisco_ios",  # Device type (IOS in this case)
        "ip": singledevice333,        # IP address of the device
        "username": user333,          # Username for SSH login
        "password": pass333,          # Password for SSH login
    }

    # Connect to device
    ssh333 = ConnectHandler(**ciscodeviceinfo333)
    print("#" * 25)
    print("Connecting to " + singledevice333)

    # Read CLI commands from file
    with open(r"C:\Users\Rohan\Documents\clilist333.txt", "r") as file:
        readclilist333 = file.read().splitlines()

    # Execute commands on the device
    for singlecli333 in readclilist333:
        print(">" * 5 + "Output for " + singlecli333)
        output333 = ssh333.send_command(singlecli333)  # Sending command to device
        print(output333)  # Printing command output
        # Generate filename based on device IP and command
        filename = f"{singledevice333}_output_{singlecli333.replace(' ', '_')}.txt"

        # Write output to file
        with open(filename, "w") as output_file:
            output_file.write(output333)

        print(f"Output saved to {filename}")

    # Disconnect from device
    ssh333.disconnect()
    print("Disconnected from " + singledevice333)
    print("#" * 25)

