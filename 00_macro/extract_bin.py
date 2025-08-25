import base64

with open("b64encoded_macro.txt") as f:
    data = f.readlines()[0].encode("UTF-8")
pt = base64.b64decode(data)


with open("SystemFailureReporter.exe", "wb") as f:
    f.write(pt)