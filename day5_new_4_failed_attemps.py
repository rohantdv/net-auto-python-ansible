# Import necessary modules
from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoTimeoutException, NetmikoAuthenticationException
import xlrd

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
                "device_type": devicetype333,
                "username": user333,
                "password": input("Enter the credentials for " + deviceip333 + ":"),
                "ip": deviceip333
            }
            ssh333 = ConnectHandler(**deviceinfo333)

            # Find the command prompt
            prompt333 = ssh333.find_prompt()
            print(prompt333)

            # Check if logged in successfully
            if ">" in prompt333 or "#" in prompt333:
                print("Successfully logged in")

                # Send configuration commands and save the output
                config777 = ssh333.send_config_set(listconfig333)
                print(config777)

                with open(r"C:\Users\Rohan\Documents\successconfig_" + deviceip333 + ".txt", "a") as backup333:
                    backup333.write("#" * 150 + "\n")
                    backup333.write("--" * 50 + "\n")
                    backup333.write(config777)
                    backup333.write("#" * 150 + "\n")
                    backup333.write("--" * 50 + "\n")


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

                # Break out of the loop once commands are executed
                break

            else:
                pass

        except NetmikoTimeoutException:
            print("Timeout issues " + deviceip333)

        except NetmikoAuthenticationException:
            print("Authentication " + deviceip333)

        end = end + 1
        print(end)

print("Job is successful")