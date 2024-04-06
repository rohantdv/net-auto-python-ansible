# Import necessary modules
from netmiko import ConnectHandler, SSHDetect  # Importing required classes from netmiko library
from netmiko.exceptions import NetmikoTimeoutException, NetmikoAuthenticationException  # Importing specific exceptions from netmiko library
import xlrd  # Importing xlrd module for working with Excel files

# Open the Excel workbook
workbook333 = xlrd.open_workbook_xls(r"C:\Users\Rohan\Documents\New Microsoft Excel Worksheet1.xls")

# Access the specific sheet within the workbook
sheet333 = workbook333.sheet_by_name("MY")

# Iterate through each row in the sheet
for singleindex333 in range(1, sheet333.nrows):
    # Extract device IP, username, password, configuration, command, and device type from each row
    deviceip333 = sheet333.row(singleindex333)[1].value
    user333 = sheet333.row(singleindex333)[4].value
    pass333 = sheet333.row(singleindex333)[5].value
    config333 = sheet333.row(singleindex333)[7].value
    command333 = sheet333.row(singleindex333)[8].value
    devicetype333 = sheet333.row(singleindex333)[3].value

    # Split configuration and command into lists
    listconfig333 = config333.split("\n")
    listcommand333 = command333.split("\n")

    # Set up a counter to limit login attempts
    end = 1

    # Try to connect to the device, handle authentication and timeout exceptions
    while end < 5:
        try:
            # Provide device information for connection
            deviceinfo333 = {
                "device_type": "autodetect",
                "username": user333,
                "password": input("Enter the credentials for " + deviceip333 + ":"),
                "ip": deviceip333
            }

            # Use SSHDetect to detect the device type
            guessuser333 = SSHDetect(**deviceinfo333)
            device_type = guessuser333.autodetect()
            print(device_type)

            # Based on the detected device type, execute specific actions
            if device_type == "cisco_ios":
                # Create device info dictionary for Cisco IOS devices
                cisco333 = {
                    "device_type": device_type,
                    "ip": deviceip333,
                    "username": user333,
                    "password": input("Enter the credentials for " + deviceip333 + ":")
                }

                # Connect to the device using ConnectHandler
                ssh333 = ConnectHandler(**cisco333)
                prompt333 = ssh333.find_prompt()
                print(prompt333)

                # If prompt contains '>' or '#', execute further actions
                if ">" in prompt333 or "#" in prompt333:
                    print("Successfully logged in")

                    # Send configuration commands and save the output
                    config999 = ssh333.send_config_set(listconfig333)
                    print(config999)

                    with open(r"C:\Users\Rohan\Documents\successconfig_" + deviceip333 + ".txt", "a") as backup999:
                        backup999.write("#" * 150 + "\n")
                        backup999.write("--" * 50 + "\n")
                        backup999.write(config999 + "\n")
                        backup999.write("\n" + "#" * 150 + "\n")
                        backup999.write("--" * 50 + "\n")

                    # Send command and save the output
                    for singlecli333 in listcommand333:
                        cli333 = ssh333.send_command(singlecli333)
                        print(cli333)

                        with open(r"C:\Users\Rohan\Documents\showcli_" + deviceip333 + ".txt", "a") as backup777:
                            backup777.write("#" * 150 + "\n")
                            backup777.write("--" * 50 + "\n")
                            backup777.write(f"Output for >>>>> {singlecli333} <<<<<\n")
                            backup777.write("--" * 50 + "\n")
                            backup777.write(cli333 + "\n")
                            backup777.write("#" * 150 + "\n")

                    break
                else:
                    pass

            # Handle other device types
            elif device_type == "panos":
                print("connect handler")
                print("show commands")
                print("config commands")
                break
            elif device_type == "linux":
                print("connect handler")
                print("show commands")
                print("config commands")
                break
            elif device_type == "cisco_asa":
                print("connect handler")
                print("show commands")
                print("config commands")
                break
            elif device_type == "fgt":
                print("connect handler")
                print("show commands")
                print("config commands")
                break
            else:
                print("no SSH device found")
        except NetmikoTimeoutException:
            print("Timeout issues " + deviceip333)
        except NetmikoAuthenticationException:
            print("Authentication " + deviceip333)

        end = end + 1
        print(end)

print("Job is successful")  # Indicating job completion
