import json, requests

text = "TheAutobotsCorp" # example text
headers = {"user-agent": "Mozilla/5.0"}
host = "https://api.imjustgood.com/base64/text="+text
data = json.loads(requests.get(host,headers=headers).text)
result = data["result"]
print(result)
