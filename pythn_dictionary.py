deviceinfo = {
    "ip":"3.3.3.3",
    "username":"admin",
    "password":"cisco",
}
print(deviceinfo)


deviceinfo1 = {
    "ip":"3.3.3.3",
    "username":"admin",
    "password":"cisco",
    "password":"cisco",
}
print(deviceinfo1)

deviceinfo = {
    "ip":"3.3.3.3",
    "username":"admin",
    "password":"cisco",
}
print(deviceinfo["password"])


deviceinfo = {
    "ip":"3.3.3.3",
    "username":"admin",
    "password":"cisco",
}
deviceinfo["password"] = "rohan123"
print(deviceinfo)