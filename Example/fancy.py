import json, requests

text = "imjustgood" # example your text
host = "https://api.imjustgood.com/fancy?text="+text
data = json.loads(requests.get(host).text)

# Get attributes
result = ""
for s in data["result"]:
    result += "\n{}\n".format(s)
print(result)

# Get JSON results
print(data)
