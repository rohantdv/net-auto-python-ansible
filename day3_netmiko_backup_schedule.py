# Importing necessary modules
from netmiko import ConnectHandler  # Module for SSH connection to network devices
import datetime  # Module for date and time operations
import schedule  # Module for task scheduling

# Define a function called job333
def job333():
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
        # Connect to the device
        ssh333 = ConnectHandler(**ciscodeviceinfo333)
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

# Schedule the job333 function to run every 10 seconds
schedule.every(10).seconds.do(job333)

# Loop indefinitely to keep running the scheduled tasks
while True:
    schedule.run_pending()
