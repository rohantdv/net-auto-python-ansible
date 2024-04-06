import json  # Importing the JSON module for data serialization

from napalm import get_network_driver  # Importing the required Napalm module
net_driver = get_network_driver("ios")  # Getting the network driver for IOS devices

import datetime

# Getting current date and time directly
customize_date_time = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")

# List of multiple devices to connect to
multi_device = ["192.168.195.242", "192.168.195.241"]

# Iterating through each device in the list
for single_device in multi_device:

    # Optional arguments for devices, in this case, providing the enable secret if configured
    optional_args = {"secret": "cisco"}

    # Connecting to the device via SSH using Napalm
    ssh_device = net_driver(hostname=single_device, username="admin", password="cisco", optional_args=optional_args)
    ssh_device.open()  # Opening SSH connection to the device
    print("Connected to " + single_device)  # Printing confirmation of successful connection

    # # Gathering information about the device's interfaces IP addresses
    # single_device_output = ssh_device.get_interfaces_ip()
    #
    # # Gathering ARP table information
    # single_device_output = ssh_device.get_arp_table()
    #
    # # Pinging a destination from the device
    # single_device_output = ssh_device.ping(destination="1.1.1.1", source=single_device, count=7)

    # Getting startup configuration from the device
    single_device_output = ssh_device.get_config()["startup"]

    # # Gathering various CLI commands output
    # single_device_output = ssh_device.cli(["show ip int br", "show ip route", "show ver | i up", "show clock"])

    print(single_device_output)  # Printing the output of the gathered information

    # # Serializing gathered data into JSON format for better readability and storage
    # json_single_device_output = json.dumps(single_device_output, sort_keys=True, indent=4)
    # print(json_single_device_output)  # Printing JSON formatted output

    # Writing the gathered information to a text file for backup
    with open(r"C:\Users\Rohan\Documents\napalm_config_backup_" + single_device + "_" + customize_date_time + ".txt", "a") as config_backup:
        config_backup.write(single_device_output)  # Writing output to the text file
