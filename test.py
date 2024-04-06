from netmiko import ConnectHandler
import re
import csv

# Define device information
devices = [
    {
        "device_type": "cisco_ios",
        "ip": "192.168.195.229",
        "username": "admin",
        "password": "cisco"
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.195.230",
        "username": "admin",
        "password": "cisco"
    },
    {
        "device_type": "cisco_ios",
        "ip": "192.168.195.231",
        "username": "admin",
        "password": "cisco"
    }
]

# Initialize an empty list to store memory information
memory_data = []

# Iterate over each device
for device in devices:
    # Connect to the device
    ssh_device = ConnectHandler(**device)
    print(f"Connected to {device['ip']}")

    # Send command to retrieve memory output
    output = ssh_device.send_command("show process memory")

    # Parse memory output using regular expressions
    total_memory_match = re.search(r"Total\s*memory:\s*(\d+)\s*KB", output)
    free_memory_match = re.search(r"Free\s*memory:\s*(\d+)\s*KB", output)

    # Extract memory information if matches are found
    if total_memory_match and free_memory_match:
        total_memory_kb = int(total_memory_match.group(1))
        free_memory_kb = int(free_memory_match.group(1))
        memory_utilization = ((total_memory_kb - free_memory_kb) / total_memory_kb) * 100
        memory_data.append({
            "Device IP": device['ip'],
            "Total Memory (KB)": total_memory_kb,
            "Free Memory (KB)": free_memory_kb,
            "Memory Utilization (%)": memory_utilization
        })
    else:
        memory_data.append({
            "Device IP": device['ip'],
            "Total Memory (KB)": "N/A",
            "Free Memory (KB)": "N/A",
            "Memory Utilization (%)": "N/A"
        })

    # Disconnect from the device
    ssh_device.disconnect()

# Write collected memory information to a CSV file
csv_file_path = "Audit_report.csv"
with open(r"C:\Users\Rohan\Documents\Audit_report_ios_upgrade.csv", mode='w', newline='') as file:
    fieldnames = ["Device IP", "Total Memory (KB)", "Free Memory (KB)", "Memory Utilization (%)"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    for data in memory_data:
        writer.writerow(data)

print(f"Memory information written to {csv_file_path}")
