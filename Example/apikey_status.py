import json, requests

apikey = "YOUR_APIKEY_HERE"
host = "https://api.imjustgood.com/status?apikey={}".format(apikey)
data = json.loads(requests.get(host).text)

# Get attributes
result = "Apikey Status"
result += "\nID : {}".format(data["result"]["id"])
result += "\nType : {}".format(data["result"]["type"])
result += "\nUsage : {}".format(data["result"]["usage"])
result += "\nExpired : {}".format(data["result"]["expired"])
result += "\nRestart : {}".format(data["result"]["restart"])
result += "\nTimeleft : {}".format(data["result"]["timeleft"])
print(result)

# Get JSON results
print(data)
