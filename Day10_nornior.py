import time
start = time.time()


from nornir import InitNornir
from nornir_netmiko.tasks import netmiko_send_command, netmiko_send_config
from nornir_napalm.plugins.tasks import napalm_get, napalm_configure
from nornir_utils.plugins.functions import print_result
from getpass import getpass

nor_task = InitNornir("config.yml")

# user = getpass("user:")
# password = getpass("password:")
# nor_task.inventory.defaults.username = user
# nor_task.inventory.defaults.password = password
#
# fetch_task = nor_task.run(task=netmiko_send_command, command_string = "show ip int br")
# print_result(fetch_task)

multi_cli = ["show run | i hostname", "show ip int br", "show ver | i up", "show clock"]

for single_cli in multi_cli:
    fetch_task = nor_task.run(netmiko_send_command, command_string=single_cli)
    # print_result(fetch_task)

# fetch_task = nor_task.run(netmiko_send_config, config_commands=["router ospf 3", "int loop 39"])
# print_result(fetch_task)

# fetch_task = nor_task.run(netmiko_send_config, config_file=r"C:\Users\Rohan\Documents\config_input.txt")
# print_result(fetch_task)

# fetch_task = nor_task.run(napalm_get,getters = ["get_facts", "get_config"])
# print_result(fetch_task)

# fetch_task = nor_task.run(napalm_configure,filename=r"C:\Users\Rohan\Documents\config_input.txt")
# print_result(fetch_task)

end = time.time()
elapsedtime = end - start
print(elapsedtime)