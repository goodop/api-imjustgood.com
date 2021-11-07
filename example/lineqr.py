from justgood import imjustgood

api     = imjustgood("YOUR_APIKEY_HERE")
data    = api.lineqr(
    appName="CHROMEOS\t2.4.7\tChromeOS\t96",
    sysName="IMJUSTGOOD",
    cert=None
)
cbpin   = data["result"]["callback"]["pin"]
cbtoken = data["result"]["callback"]["token"]
qrlink  = data["result"]["qr"]
print(qrlink)

data    = api.lineqrGetPin(cbpin)
if data["status"] == 200:
    pin = data["result"]["pin"]
    print(pin)

data    = api.lineqrGetToken(cbtoken)
result  = "Application : {}\n\n".format(data["result"]["app"])
result += "Certified : {}\n\n".format(data["result"]["cert"])
result += "Authtoken : {}".format(data["result"]["token"])
print(result)
