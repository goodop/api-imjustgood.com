from justgood import imjustgood

api    = imjustgood("YOUR_APIKEY_HERE")
data   = api.lineqr(appName="CHROMEOS\t2.4.5\tChromeOS\t1", sysName="JUSTGOOD", cert=None)
cbpin  = data["result"]["callback"]["pin"]
cbaut  = data["result"]["callback"]["token"]
linkqr = data["result"]["qr"]
print(linkqr)

data = api.lineqrGetPin(cbpin)
if data["status"] == 200:
    pin = data["result"]["pin"]
    print(pin)

data = api.lineqrGetToken(cbaut)
result = "Certified : {}\n\n".format(data["result"]["cert"])
result += "Authtoken : {}".format(data["result"]["token"])
print(result)
