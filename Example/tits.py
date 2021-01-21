from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
data = media.tits()

# Get attributes
result = "Tits Analyze"
result += "\nTits : {}".format(data["result"]["tits"])
result += "\nSize : {}{}".format(data["result"]["size"],data["result"]["cup"])
result += "\nNipple : {}".format(data["result"]["nipple"])
result += "\nAerola : {}".format(data["result"]["aerola"])
result += "\nDescription : {}".format(data["result"]["description"])
result += "\nPicture : {}".format(data["result"]["picture"])
print(result)

# Get JSON results
print(data)
