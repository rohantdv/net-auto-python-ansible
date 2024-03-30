# Import necessary modules
from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoTimeoutException, NetmikoAuthenticationException
import datetime
import xlrd

# Get current date and time
now333 = datetime.datetime.now()
date333 = now333.day
month333 = now333.month
year333 = now333.year
hours333 = now333.hour
min333 = now333.minute
sec333 = now333.second
customizedate333 = str(date333) + "_" + str(month333) + "_" + str(year333) + "_" + str(hours333) + "_" + str(min333) + "_" + str(sec333)

try:
    # Open the Excel file
    book333 = xlrd.open_workbook(r"C:\Users\Rohan\Documents\New Microsoft Excel Worksheet1.xls")
    sheet333 = book333.sheet_by_name("MY")
except FileNotFoundError:
    # Handle file not found exception
    print("Excel file not found.")
    exit()

# Iterate through each row in the Excel sheet
for singleindex333 in range(1, sheet333.nrows):
    # Extract device information from Excel sheet
    deviceip333 = sheet333.row(singleindex333)[1].value
    devicetype333 = sheet333.row(singleindex333)[3].value
    username333 = sheet333.row(singleindex333)[4].value
    password333 = sheet333.row(singleindex333)[5].value
    config333 = sheet333.row(singleindex333)[7].value
    listconfig333 = config333.split("\n")
    showcli333 = sheet333.row(singleindex333)[8].value
    listshowcli333 = showcli333.split("\n")

    try:
        # Define device information for connecting via SSH
        ciscodeviceinfo333 = {
            "device_type": devicetype333,
            "ip": deviceip333,
            "username": username333,
            "password": password333
        }

        # Connect to device via SSH
        ssh333 = ConnectHandler(**ciscodeviceinfo333)
        # Send configuration commands to the device
        config3334 = ssh333.send_config_set(listconfig333)

        # Log successful SSH connection
        with open(r"C:\Users\Rohan\Documents\ssh_success" + "-" + customizedate333 + ".txt", "a") as ssh_success333:
            ssh_success333.write(deviceip333 + "\n")

        # Get prompt from device
        host333 = ssh333.find_prompt()
        newhost333 = host333.strip("#")
        print("#" * 50)
        print("Connecting to " + deviceip333)
        print("#" * 50)

        # Backup configuration of the device
        with open(r"C:\Users\Rohan\Documents\send_config_set_ " + deviceip333 + "-" + newhost333 + "-" + customizedate333 + ".txt", "a") as backup333:
            backup333.write("#" * 150 + "\n")
            backup333.write(config3334 + "\n")
            backup333.write("#" * 150 + "\n")

        # Execute show commands and backup output
        for sincli333 in listshowcli333:
            cli_output = ssh333.send_command(sincli333)

            with open(r"C:\Users\Rohan\Documents\show_cli_backup_" + deviceip333 + "-" + newhost333 + "-" + customizedate333 + ".txt", "a") as backup3334:
                backup3334.write("#" * 150 + "\n")
                backup3334.write(">" * 5 + "Output for " + sincli333 + "\n")
                backup3334.write(cli_output + "\n")
                backup3334.write("#" * 150 + "\n")

        # Disconnect from device
        ssh333.disconnect()
        print("Disconnected from " + deviceip333)
        print("#" * 50)

    except NetmikoAuthenticationException:
        # Handle authentication failure
        print(deviceip333 + " password issue!")
        with open(r"C:\Users\Rohan\Documents\auth_password_issue" + "-" + customizedate333 + ".txt", "a") as authentication333:
            authentication333.write(deviceip333 + "\n")

    except NetmikoTimeoutException:
        # Handle timeout exception
        print(deviceip333 + " timeout issue!")
        with open(r"C:\Users\Rohan\Documents\timeout_issue" + "-" + customizedate333 + ".txt", "a") as timeout333:
            timeout333.write(deviceip333 + "\n")
