import time, json, requests

# Line Version Info https://api.imjustgood.com/line

apikey = "YOUR_APIKEY_HERE"
cert = None # if you have a cert code put here
appname = "CHROMEOS\t2.4.4\tChromeOS\t88" # example app name
sysname = "JUSTGOOD" # example system name
headers = {"apikey": apikey, "appName": appName, "sysName": sysName, "cert": cert}
host = "https://api.imjustgood.com/lineqr"

data = json.loads(requests.get(host,headers=headers).text)
print(data["result"]["qr"])
if cert is None:
    for i in range(10):
        main = json.loads(requests.get(data["result"]["callback"]["pin"],headers=headers).text)
        if main["status"] == 200:
            print(main["result"]["pin"])
            break
        elif i == 9:
            print(main["message"])
            break
        else:time.sleep(1)
for i in range(10):
    main = json.loads(requests.get(data["result"]["callback"]["token"],headers=headers).text)
    if main["status"] == 200:
        print(main["result"]["token"])
        print(main["result"]["cert"])
        break
    elif i == 9:
        print(main["message"])
        break
    else:time.sleep(1)
