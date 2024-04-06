# Import necessary modules
from netmiko import ConnectHandler
from netmiko.ssh_autodetect import SSHDetect
from netmiko.ssh_autodetect import guess_device_type
from netmiko.exceptions import NetmikoTimeoutException, NetmikoAuthenticationException
import datetime
import xlrd

# Get current date and time
now = datetime.datetime.now()
customizedate = now.strftime("%d_%m_%Y_%H_%M_%S")

try:
    # Open the Excel file
    book = xlrd.open_workbook(r"C:\Users\Rohan\Documents\New Microsoft Excel Worksheet1.xls")
    sheet333 = book.sheet_by_name("MY")
except FileNotFoundError:
    # Handle file not found exception
    print("Excel file not found.")
    exit()

# Iterate through each row in the Excel sheet
for singleindex333 in range(1, sheet333.nrows):
    # Extract device information from Excel sheet
    deviceip333, username333, password333, config333, showcli333 = sheet333.row_values(singleindex333, start_colx=1, end_colx=9)
    listconfig333 = config333.split("\n")
    listshowcli333 = showcli333.split("\n")

    try:
        # Auto-detect device type
        detector = SSHDetect(device=deviceip333, user=username333, password=password333)
        best_match = guess_device_type(detector)

        # Define device information for connecting via SSH
        device_info = {
            "device_type": best_match,
            "ip": deviceip333,
            "username": username333,
            "password": password333
        }

        # Connect to device via SSH
        with ConnectHandler(**device_info) as ssh:
            # Send configuration commands to the device
            config_output = ssh.send_config_set(listconfig333)

            # Log successful SSH connection
            with open(f"C:/Users/Rohan/Documents/ssh_success-{customizedate}.txt", "a") as ssh_success:
                ssh_success.write(f"{deviceip333}\n")

            # Get prompt from device
            host = ssh.find_prompt()
            new_host = host.strip("#")
            print("#" * 50)
            print(f"Connecting to {deviceip333}")
            print("#" * 50)

            # Backup configuration of the device
            with open(f"C:/Users/Rohan/Documents/send_config_set_{deviceip333}-{new_host}-{customizedate}.txt", "a") as backup:
                backup.write("#" * 150 + "\n")
                backup.write(config_output + "\n")
                backup.write("#" * 150 + "\n")

            # Execute show commands and backup output
            for cli_command in listshowcli333:
                cli_output = ssh.send_command(cli_command)

                with open(f"C:/Users/Rohan/Documents/show_cli_backup_{deviceip333}-{new_host}-{customizedate}.txt", "a") as backup:
                    backup.write("#" * 150 + "\n")
                    backup.write("--" * 50 + "\n")
                    backup.write(f"Output for >>>>> {cli_command} <<<<<\n")
                    backup.write("--" * 50 + "\n")
                    backup.write(cli_output + "\n")
                    backup.write("#" * 150 + "\n")

            print(f"Disconnected from {deviceip333}")
            print("#" * 50)

    except NetmikoAuthenticationException:
        # Handle authentication failure
        print(f"{deviceip333} authentication failed!")
        with open(f"C:/Users/Rohan/Documents/auth_password_issue-{customizedate}.txt", "a") as authentication:
            authentication.write(f"{deviceip333}\n")

    except NetmikoTimeoutException:
        # Handle timeout exception
        print(f"{deviceip333} connection timed out!")
        with open(f"C:/Users/Rohan/Documents/timeout_issue-{customizedate}.txt", "a") as timeout:
            timeout.write(f"{deviceip333}\n")
