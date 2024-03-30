# Importing necessary modules
from netmiko import ConnectHandler  # Module for SSH connection to network devices
from netmiko.exceptions import NetmikoTimeoutException, NetmikoAuthenticationException
import datetime  # Module for date and time operations
import logging  # Importing the logging module for generating log files

# Configuring the logging module
logging.basicConfig(filename="python_debug_log", level=logging.DEBUG)

# Creating a logger object named 'logger333' for the 'netmiko' component
logger333 = logging.getLogger("netmiko")

# Get current date and time
now333 = datetime.datetime.now()
# Extract date, month, year, hours, minutes, and seconds
date333 = now333.day
month333 = now333.month
year333 = now333.year
hours333 = now333.hour
min333 = now333.minute
sec333 = now333.second
# Format the date and time as a string
customizedate333 = str(date333) + "_" + str(month333) + "_" + str(year333) + "_" + str(hours333) + "_" + str(min333) + "_" + str(sec333)

# Read credentials from a file
with open(r"C:\Users\Rohan\Documents\devicecreds.txt", "r") as file:
    devicecreds333 = file.read().splitlines()
# Extract username and password from the credentials
user333 = devicecreds333[0]  # Username
pass333 = devicecreds333[1]  # Password

# Read a list of device IP addresses from a file
with open(r"C:\Users\Rohan\Documents\devicelist.txt", "r") as file:
    readdevicelist333 = file.read().splitlines()
# Check if the device list is empty
if not readdevicelist333:
    print("No devices found in devicelist.txt")
    exit()

# Iterate over devices in the list
for singledevice333 in readdevicelist333:
    # Configuration dictionary for a Cisco device
    ciscodeviceinfo333 = {
        "device_type": "cisco_ios",  # Device type (IOS in this case)
        "ip": singledevice333,        # IP address of the device
        "username": user333,          # Username for SSH login
        "password": pass333,          # Password for SSH login
    }
    try:
        # Connect to the device
        ssh333 = ConnectHandler(**ciscodeviceinfo333)
        ssh_success333 = open(r"C:\Users\Rohan\Documents\ssh_success" + "-" + customizedate333 + ".txt", "a")
        ssh_success333.write(singledevice333 + "\n")
        ssh_success333.close

        host333 = ssh333.find_prompt()
        newhost333 = host333.strip("#")
        print("#" * 25)
        print("Connecting to " + singledevice333)

        # Read CLI commands from a file
        with open(r"C:\Users\Rohan\Documents\clilist333.txt", "r") as file:
            readclilist333 = file.read().splitlines()
        # Execute commands on the device
        for singlecli333 in readclilist333:
            print(">" * 5 + "Output for " + singlecli333)
            output333 = ssh333.send_command(singlecli333)  # Sending command to the device
            print(output333)  # Printing command output

            # Taking a backup
            backup333 = open(r"C:\Users\Rohan\Documents\config_backup_ " + singledevice333 + "-" + newhost333 + "-" + customizedate333 + ".txt", "a")
            backup333.write(">" * 5 + "Output for " + singlecli333)
            backup333.write("\n" + output333 + "\n")
            backup333.close()

        # Disconnect from the device
        ssh333.disconnect()
        print("Disconnected from " + singledevice333)
        print("#" * 25)

    except NetmikoAuthenticationException:
        print(singledevice333 + " password issue!")
        authentication333 = open(r"C:\Users\Rohan\Documents\auth_password_issue" + "-" + customizedate333 + ".txt", "a")
        authentication333.write(singledevice333 + "\n")
        authentication333.close
    except NetmikoTimeoutException:
        print(singledevice333 + " timeout issue!")
        timeout333 = open(r"C:\Users\Rohan\Documents\timeout_issue" + "-" + customizedate333 + ".txt", "a")
        timeout333.write(singledevice333 + "\n")
        timeout333.close
