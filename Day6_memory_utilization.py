import re
from netmiko import ConnectHandler
import csv
import os


multi_devices = ["192.168.195.235", "192.168.195.236", "192.168.195.237"]


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

    io_pool = re.compile(r'I/O Pool Total:\s+(\d+)\s+Used:\s+(\d+)\s+Free:\s+(\d+)')
    final_io_pool = io_pool.findall(z)

    if final_io_pool:
        for memory_data in final_io_pool:

            Total, Used, Free = memory_data

            memory_utilization = (int(Free) / int(Total)) * 100

            file_exist = os.path.isfile(r"C:\Users\Rohan\Documents\Audit_report.csv")

            with open(r"C:\Users\Rohan\Documents\Audit_report.csv", "a", newline="") as csv_file:
                header = ["IP ADDRESS", "HOSTNAME", "CURRENT IOS RUNNING VERSION", "SYSTEM PATH", "UPTIME", "RELOAD REASONS", "SERIAL ID", "CONFIG REGISTER", "TOTAL MEMORY", "USED MEMORY", "FREE MEMORY", "MEMORY UTILIZATION"]
                writer = csv.DictWriter(csv_file, fieldnames=header)

                if file_exist:
                    writer.writerow({
                        "IP ADDRESS": single_device,
                        "CURRENT IOS RUNNING VERSION": final_target_version,
                        "HOSTNAME": final_hostname,
                        "SYSTEM PATH": final_system_image_file,
                        "UPTIME": final_uptime,
                        "RELOAD REASONS": final_reload_reason,
                        "SERIAL ID": final_serial_id,
                        "CONFIG REGISTER": final_config_reg,
                        "TOTAL MEMORY": Total,
                        "USED MEMORY": Used,
                        "FREE MEMORY": Free,
                        "MEMORY UTILIZATION": f"{memory_utilization}%"
                    })

                else:
                    writer.writeheader()
                    writer.writerow({
                        "IP ADDRESS": single_device,
                        "CURRENT IOS RUNNING VERSION": final_target_version,
                        "HOSTNAME": final_hostname,
                        "SYSTEM PATH": final_system_image_file,
                        "UPTIME": final_uptime,
                        "RELOAD REASONS": final_reload_reason,
                        "SERIAL ID": final_serial_id,
                        "CONFIG REGISTER": final_config_reg,
                        "TOTAL MEMORY": Total,
                        "USED MEMORY": Used,
                        "FREE MEMORY": Free,
                        "MEMORY UTILIZATION": f"{memory_utilization}%"
                    })


print("Job is successful!")
