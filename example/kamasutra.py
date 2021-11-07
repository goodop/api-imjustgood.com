from justgood import imjustgood

api     = imjustgood("YOUR_APIKEY_HERE")
data    = api.kamasutra()
print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES
result  = "Style : {}".format(data["result"]["style"])
result += "\nDescription :\n{}".format(data["result"]["description"])
result += "\nPicture : {}".format(data["result"]["thumbnail"])
print(result)
