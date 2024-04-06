"""
This script connects to multiple Cisco IOS devices using SSH, retrieves configuration information,
and saves the configuration along with the output of specified commands to an Excel file.

Dependencies:
- netmiko: For SSH connectivity to network devices.
- xlwt: For creating Excel files.

Instructions:
1. Install dependencies: Run `pip install netmiko xlwt`.
2. Update the 'multidevices333' list with the IP addresses of the Cisco IOS devices.
3. Ensure that the provided username and password have the necessary permissions to access the devices.
4. Run the script.
5. The script will create an Excel file for each device containing its configuration and specified command outputs.
"""

from netmiko import ConnectHandler
import xlwt

# List of Cisco IOS devices' IP addresses
multidevices333 = ["192.168.195.220", "192.168.195.221", "192.168.195.222"]

# Iterate over each device
for singledevice333 in multidevices333:
    # Device connection information
    deviceinfo333 = {
        "device_type": "cisco_ios",
        "ip": singledevice333,
        "username": "admin",
        "password": "cisco"
    }

    # Establish SSH connection to the device
    ssh333 = ConnectHandler(**deviceinfo333)
    prompt333 = ssh333.find_prompt()
    print(prompt333)

    # Send configuration commands to the device
    config333 = ssh333.send_config_set(["logging host 1.1.1.1", "logging host 3.3.3.3", "router ospf 100"])
    print(config333)

    # List of commands to retrieve information from the device
    listshowcli333 = ["show ver", "show ip int br", "show clock"]

    # Create a new Excel workbook and sheet for the device
    workbook333 = xlwt.Workbook()
    sheet333 = workbook333.add_sheet(singledevice333 + "-" + prompt333)
    row = 2
    col = 2

    # Write device configuration to the Excel sheet
    listconfig333 = config333.splitlines()
    for x123 in listconfig333:
        sheet333.write(row, col, x123)
        row += 1

    # Write command outputs to the Excel sheet
    for singlecli333 in listshowcli333:
        cli333 = ssh333.send_command(singlecli333)
        print(cli333)
        sheet333.write(row, col, "######>>>" + singlecli333 + str("<<<######"))
        row += 1
        # Split CLI output by newline characters and write each line to a new row
        for line in cli333.split('\n'):
            sheet333.write(row, col, line)
            row += 1

    workbook333.save(r"C:\Users\Rohan\Documents\xlwtBackup " + singledevice333 + ".xls")

print("Job is successful")
