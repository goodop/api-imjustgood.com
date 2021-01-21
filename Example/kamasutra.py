from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
data = media.kamasutra()

# Get attributes
result = "Kamasutra"
result += "\nStyle : {}".format(data["result"]["style"])
result += "\nDescription :\n{}".format(data["result"]["description"])
result += "\nPicture : {}".format(data["result"]["thumbnail"])
print(result)

# Get JSON results
print(data)
