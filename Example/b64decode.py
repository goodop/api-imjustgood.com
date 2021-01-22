import json, requests

code = "VGhlQXV0b2JvdHNDb3Jw" # example base64 code
host = "https://api.imjustgood.com/base64/code="+code
data = json.loads(requests.get(host).text)
result = data["result"]
print(result)
