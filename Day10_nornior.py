import time  # Import the time module for measuring execution time

# Start measuring the execution time
start = time.time()

# Import necessary modules and functions
from nornir import InitNornir  # Nornir for network automation
from nornir_netmiko.tasks import netmiko_send_command, netmiko_send_config  # Netmiko tasks for sending commands and configurations
from nornir_napalm.plugins.tasks import napalm_get, napalm_configure  # Napalm tasks for retrieving and configuring network devices
from nornir_utils.plugins.functions import print_result  # Function for printing results
from getpass import getpass  # Function for securely inputting passwords

# Initialize Nornir with the provided inventory file
nor_task = InitNornir("config.yml")

# Input username and password securely
user = getpass("user:")
password = getpass("password:")
nor_task.inventory.defaults.username = user
nor_task.inventory.defaults.password = password

# Task to fetch and print the output of 'show ip interface brief' command
fetch_task = nor_task.run(task=netmiko_send_command, command_string="show ip int br")
print_result(fetch_task)

# List of multiple commands to be executed
multi_cli = ["show run | i hostname", "show ip int br", "show ver | i up", "show clock"]

# Loop through each command, fetch and print the output
for single_cli in multi_cli:
    fetch_task = nor_task.run(netmiko_send_command, command_string=single_cli)
    print_result(fetch_task)

# Task to send configuration commands directly
fetch_task = nor_task.run(netmiko_send_config, config_commands=["router ospf 3", "int loop 39"])
print_result(fetch_task)

# Task to send configuration commands stored in a file
fetch_task = nor_task.run(netmiko_send_config, config_file=r"C:\Users\Rohan\Documents\config_input.txt")
print_result(fetch_task)

# Task to retrieve network device information (facts and config) using Napalm
fetch_task = nor_task.run(napalm_get, getters=["get_facts", "get_config"])
print_result(fetch_task)

# Task to configure network devices using Napalm, with configuration stored in a file
fetch_task = nor_task.run(napalm_configure, filename=r"C:\Users\Rohan\Documents\config_input.txt")
print_result(fetch_task)

# End measuring the execution time and calculate elapsed time
end = time.time()
elapsedtime = end - start
print("Elapsed time:", elapsedtime)  # Print the elapsed time
