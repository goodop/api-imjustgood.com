from justgood import imjustgood

api  = imjustgood("YOUR_APIKEY_HERE")
data = api.mimpi("ciuman")
print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES
result = "Arti Mimpi"
for a in data["result"]:
    result += "\n\nMimpi : {}".format(a["dream"])
    result += "\nArti : {}".format(a["meaning"])
print(result)
