with open("svchost.exe", "rb") as f:
    data = f.read()

target = data[0x32c2d6:0x32c2d6+8472]
print(target[1668:1668+7])
