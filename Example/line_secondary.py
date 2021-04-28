from justgood import imjustgood
import time, json, requests

# Line Version Info https://api.imjustgood.com/line

apikey = "YOUR_APIKEY_HERE"
appname = "CHROMEOS\t2.4.4\tChromeOS\t88" # example app name
sysname = "JUSTGOOD" # example system name
cert = None # if you have a cert code put here
headers = {"apikey": apikey, "appName": appName, "sysName": sysName, "cert": cert}

media = imjustgood(apikey)
data = media.lineqr(appname)
timeour = 10

qr_link = data["result"]["qr"]
print(qr_link)

if cert is None:
    for i in range(timeout):
        main = json.loads(requests.get(data["result"]["callback"]["pin"],headers=headers).text)
        if main["status"] == 200:
            print(main["result"]["pin"])
            break
        elif i == timeout-1:
            print(main["message"])
            break
        else:time.sleep(1)

for i in range(timeout):
    main = json.loads(requests.get(data["result"]["callback"]["token"],headers=headers).text)
    if main["status"] == 200:
        print(main["result"]["token"])
        print(main["result"]["cert"])
        break
    elif i == timeout-1:
        print(main["message"])
        break
    else:time.sleep(1)
