with open("svchost.exe", "rb") as f:
    data = f.read()

target = data[0x32c2d6:0x32c2d6+8472]

png = data[0x588BE0:0x61e4d0]
with open("img.png", "wb") as f:
    f.write(png)