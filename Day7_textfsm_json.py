from netmiko import ConnectHandler
import json
import csv
import re
import os

multi_devices = ["192.168.195.235", "192.168.195.236", "192.168.195.237"]

file_exists = os.path.isfile(r"C:\Users\Rohan\Documents\Interface_Description_Addition_Report.csv")

with open(r"C:\Users\Rohan\Documents\Interface_Description_Addition_Report.csv", "a", newline="") as csv_file:
    header = ["HOSTNAME", "IP ADDRESS", "INTERFACE NAME", "INTERFACE STATUS", "INTERFACE DESCRIPTION"]
    writer = csv.DictWriter(csv_file, fieldnames=header)

    if not file_exists:
        writer.writeheader()

    for single_device in multi_devices:
        device_info = {
            "device_type": "cisco_ios",
            "ip": single_device,
            "username": "admin",
            "password": "cisco"
        }

        ssh_device = ConnectHandler(**device_info)
        print("Connected to " + single_device)

        show_version = ssh_device.send_command("show version")

        hostname = re.compile(r"(.+)\suptime")
        final_hostname = hostname.findall(show_version)[0]
        print(final_hostname)

        command = ssh_device.send_command("show ip interface brief", use_textfsm=True)
        print(json.dumps(command, indent=4))

        interface_down = [item["interface"] for item in command if item["proto"] == "down"]
        print(interface_down)

        for interface_id in interface_down:
            add_int_description = ssh_device.send_config_set(["interface " + interface_id, "description ***SPARE***"])
            print(add_int_description)

        show_int_desc_output = ssh_device.send_command("show int description", use_textfsm=True)
        print(json.dumps(show_int_desc_output, indent=4))

        for interface in show_int_desc_output:
            final_int_name = interface["port"]
            final_int_status = interface["status"]
            final_int_desc = interface["description"]

            writer.writerow({
                "IP ADDRESS": single_device,
                "HOSTNAME": final_hostname,
                "INTERFACE NAME": final_int_name,
                "INTERFACE STATUS": final_int_status,
                "INTERFACE DESCRIPTION": final_int_desc
            })

print("Job is successful!")