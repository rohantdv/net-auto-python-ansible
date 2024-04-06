# Importing necessary libraries
from netmiko import ConnectHandler
import time
import difflib

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

    # List of commands to execute before and after configuration change
    commands = ["show ip int br", "show run | sec ospf", "show clock", "show ver | i up"]

    # Pre-configuration checks
    for single_command in commands:
        # Execute command and capture output
        x = ssh_device.send_command(single_command)

        # Write command and output to pre-check file
        pre_check = open(r"C:\Users\Rohan\Documents\pre_check_" + single_device + ".txt", "a")
        write_pre_check = pre_check.write(single_command + "\n")
        write_pre_check = pre_check.write(x + "\n")
        pre_check.close()

        # Read pre-check file content
        pre_check_read = open(r"C:\Users\Rohan\Documents\pre_check_" + single_device + ".txt", "r")
        pre_check_read_split = pre_check_read.read().splitlines()

    # Push configuration changes
    push_config = ssh_device.send_config_set([
        "no int loop 110",
        "no int loop 120",
        "int loop 130",
        "int loop 140",
        "no router ospf 30",
        "router ospf 20",
        "router ospf 10"
    ])

    # Wait for configuration changes to take effect
    time.sleep(3)

    # Post-configuration checks
    for single_command in commands:
        # Execute command and capture output
        y = ssh_device.send_command(single_command)

        # Write command and output to post-check file
        post_check = open(r"C:\Users\Rohan\Documents\post_check_" + single_device + ".txt", "a")
        write_post_check = post_check.write(single_command + "\n")
        write_post_check = post_check.write(y + "\n")
        post_check.close()

        # Read post-check file content
        post_check_read = open(r"C:\Users\Rohan\Documents\post_check_" + single_device + ".txt", "r")
        post_check_read_split = post_check_read.read().splitlines()

    # Generate HTML diff report
    diff_report = difflib.HtmlDiff().make_file(pre_check_read_split, post_check_read_split)
    diff_file_location = open(r"C:\Users\Rohan\Documents\html_diff_" + single_device + ".html", "a")
    diff_file_location.write(diff_report)
    diff_file_location.close()

# Completion message
print("Job is completed!")