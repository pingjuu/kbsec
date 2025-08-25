with open("svchost.exe", "rb") as f:
    data = f.read()

png = data[0x588BE0:0x61e4d0]
with open("img.png", "wb") as f:
    f.write(png)