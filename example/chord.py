from justgood import imjustgood

api     = imjustgood("YOUR_APIKEY_HERE")
data    = api.chord("stay")
print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES
result  = "{}".format(data["result"]["title"])
result += "\n\n{}".format(data["result"]["chord"])
print(result)
