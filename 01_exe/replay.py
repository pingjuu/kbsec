import requests
import json

url = "http://182.228.44.206/"   # Wireshark에서 확인된 Host + Path
headers = {
    "Host": "drmon.chickenkiller.com",  # 패킷에 나온 Host 헤더
    "User-Agent": "Go-http-client/1.1",
    "Content-Type": "application/json",
    "Accept-Encoding": "gzip",
}

data = {
    "enc_data": "58aa92364c20a88d3de54c9cd440390daddffc952a4c3bfe0f23551bf2fc15a...",  # 실제 패킷에서 추출한 값 전체 넣기
    "id": "a492a5b0-19fb-47e1-8bb12-fc5e9351963"  # Recovery Key
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print("Status:", response.status_code)
print("Response:", response.text)