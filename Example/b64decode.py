import json, requests

code = "VGhlQXV0b2JvdHNDb3Jw" # example base64 code
headers = {"user-agent": "Justgood/5.0"}
host = "https://api.imjustgood.com/base64/code="+code
data = json.loads(requests.get(host,headers=headers).text)
result = data["result"]
print(result)
