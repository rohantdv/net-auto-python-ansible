# Importing necessary libraries
from netmiko import ConnectHandler
import pandas as pd

# List of multiple devices to connect to
multi_devices = ["192.168.195.238", "192.168.195.239", "192.168.195.240"]

# Looping through each device
for single_device in multi_devices:
    # Device information required for connection
    device_info = {
        "device_type": "cisco_ios",
        "ip": single_device,
        "username": "admin",
        "password": "cisco"
    }

    # Establishing SSH connection to the device
    ssh_device = ConnectHandler(**device_info)
    print("Connected to " + single_device)

    # Retrieving output of 'show ip int br' command
    interface_output = ssh_device.send_command("show ip int br")

    # Splitting the output into a list of lines
    interface_output_list = interface_output.splitlines()

    # Removing the header line from the output
    skip_header = [line.split() for line in interface_output_list[1:]]

    # Column names for the Excel sheet
    columns_excel = ["INTERFACE", "IP", "OK", "METHOD", "STATUS", "PROTOCOL"]

    # Creating a DataFrame from the output data
    data_frame = pd.DataFrame(skip_header, columns=columns_excel)

    # Filtering interfaces with status 'down'
    filter_down_interfaces = data_frame[data_frame["STATUS"] == "down"]

    # Saving the filtered DataFrame to an Excel file
    filter_down_interfaces.to_excel(r"C:\Users\Rohan\Documents\Interface_Down_report_" + single_device + ".xlsx")

# Completion message
print("Job is successfully completed!")