from justgood import imjustgood

api       = imjustgood("YOUR_APIKEY_HERE")
data      = api.check_ip("8.8.8.8")
print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES
result    = "Ip Address : {}".format(data["result"]["ip_address"])
for a in data["result"]:
    if a != "ip_address" and a != "languages" and data["result"][a] is not None:
       result += "\n{} : {}".format(a.title(),data["result"][a])
languages = "\nLanguage : "
for b in data["result"]["languages"]:
    languages += "{}, ".format(b)
result   += languages[:-2]
print(result)
