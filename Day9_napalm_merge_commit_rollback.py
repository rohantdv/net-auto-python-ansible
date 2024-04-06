from napalm import get_network_driver
net_driver = get_network_driver("ios")

multi_device = ["192.168.195.242", "192.168.195.241"]

for single_device in multi_device:

    optional_args = {"secret": "cisco"}

    ssh_device = net_driver(hostname=single_device, username="admin", password="cisco", optional_args=optional_args)
    ssh_device.open()
    print("Connected to " + single_device)

    ssh_device.load_merge_candidate(r"C:\Users\Rohan\Documents\napalm_device_config_input.txt")
    diff_config = ssh_device.compare_config()
    print(diff_config)

    if len(diff_config) > 0:
        question_config = input("Do you really want to apply the config right away? :")
        if question_config == "yes":
            ssh_device.commit_config()
        else:
            print("Not right now")
            ssh_device.discard_config()
    else:
        print("No config difference found!")

    question_rollback_config = input("Do you want to rollback? :")
    if question_rollback_config == "yes":
        ssh_device.rollback()
    else:
        print("No rollback needed!")
