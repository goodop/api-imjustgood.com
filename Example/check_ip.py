import json, requests

ip_address = "8.8.8.8" # example ip address
host = "https://api.imjustgood.com/ip="+ip_address
data = json.loads(requests.get(host).text)

# Get attributes
result = "Ip Address : {}".format(data["result"]["ip_address"])
for a in data["result"]:
    if a != "ip_address" and a != "languages" and data["result"][a] is not None:
       result += "\n{} : {}".format(a.title(),data["result"][a])
languages = "\nLanguage : "
for b in data["result"]["languages"]:
    languages += "{}, ".format(b)
result += languages[:-2]
print(result)

# Get JSON results
print(data)
