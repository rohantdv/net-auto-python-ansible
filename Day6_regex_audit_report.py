from netmiko import ConnectHandler
import re
import csv
import os

multi_devices = ["192.168.195.229", "192.168.195.230", "192.168.195.231"]

for single_device in multi_devices:
    device_info = {
        "device_type": "cisco_ios",
        "ip": single_device,
        "username": "admin",
        "password": "cisco"
    }

    ssh_device = ConnectHandler(**device_info)
    print("Connected to " + single_device)

    x = ssh_device.send_command("show version")
    y = ssh_device.send_command("show run")
    z = ssh_device.send_command("show process memory")

    target_version = re.compile(r"Version\s*(.+)")
    final_target_version = target_version.findall(x)[0]
    print(final_target_version)

    uptime = re.compile(r"uptime\s\s*is\s(.+)")
    final_uptime = uptime.findall(x)[0]
    print(final_uptime)

    serial_id = re.compile(r"Processor\s*board\s*ID\s*(.+)")
    final_serial_id = serial_id.findall(x)[0]
    print(final_serial_id)

    system_image_file = re.compile(r'System\s*image\s*file\s*is\s*"(.+)"')
    final_system_image_file = system_image_file.findall(x)[0]
    print(final_system_image_file)

    reload_reason = re.compile(r"Last\s*reload\s*reason:\s*(.+)")
    final_reload_reason = reload_reason.findall(x)[0]
    print(final_reload_reason)

    config_reg = re.compile(r"Configuration\s*register\s*is\s*(.+)")
    final_config_reg = config_reg.findall(x)[0]
    print(final_config_reg)

    hostname = re.compile(r"(.+)\suptime")
    final_hostname = hostname.findall(x)[0]
    print(final_hostname)

    file_exist = os.path.isfile(r"C:\Users\Rohan\Documents\Audit_report_ios_upgrade.csv")

    if file_exist:

        with open(r"C:\Users\Rohan\Documents\Audit_report_ios_upgrade.csv", "a", newline="") as csv_file:
            header = ["IP ADDRESS", "HOSTNAME", "CURRENT IOS RUNNING VERSION", "SYSTEM PATH", "UPTIME", "RELOAD REASONS", "SERIAL ID", "CONFIG REGISTER"]
            writer = csv.DictWriter(csv_file, fieldnames=header)
            writer.writerow({
                "IP ADDRESS":single_device,
                "CURRENT IOS RUNNING VERSION": final_target_version,
                "HOSTNAME": final_hostname,
                "SYSTEM PATH": final_system_image_file,
                "UPTIME": final_uptime,
                "RELOAD REASONS": final_reload_reason,
                "SERIAL ID": final_serial_id,
                "CONFIG REGISTER": final_config_reg
            })

    if not file_exist:

        with open(r"C:\Users\Rohan\Documents\Audit_report_ios_upgrade.csv", "a", newline="") as csv_file:
            header = ["IP ADDRESS", "HOSTNAME", "CURRENT IOS RUNNING VERSION", "SYSTEM PATH", "UPTIME", "RELOAD REASONS", "SERIAL ID", "CONFIG REGISTER"]
            writer = csv.DictWriter(csv_file, fieldnames=header)
            writer.writeheader()
            writer.writerow({
                "IP ADDRESS":single_device,
                "CURRENT IOS RUNNING VERSION": final_target_version,
                "HOSTNAME": final_hostname,
                "SYSTEM PATH": final_system_image_file,
                "UPTIME": final_uptime,
                "RELOAD REASONS": final_reload_reason,
                "SERIAL ID": final_serial_id,
                "CONFIG REGISTER": final_config_reg
            })

print("Job is successful!")




