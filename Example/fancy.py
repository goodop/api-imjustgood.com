import json, requests

text = "imjustgood" # example your text
headers = {"user-agent": "Justgood/5.0"}
host = "https://api.imjustgood.com/fancy?text="+text
data = json.loads(requests.get(host,headers=headers).text)

# Get attributes
result = ""
for s in data["result"]:
    result += "\n{}\n".format(s)
print(result)

# Get JSON results
print(data)
