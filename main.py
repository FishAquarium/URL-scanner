import requests

url = "https://www.virustotal.com/api/v3/files"

payload = "-----011000010111000001101001--\r\n\r\n"
headers = {
    "Accept": "application/json",
    "Content-Type": "multipart/form-data; boundary=---011000010111000001101001",
    "x-apikey": "68850b90b2b305705c4f2abc9222a790c1f4395c6d148d51f31a5c7913805808",
    "File": "/hello.txt"
}

response = requests.post(url, data=payload, headers=headers)

print(response.text)