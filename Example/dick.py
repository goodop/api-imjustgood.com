from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
data = media.dick()

# Get attributes
result = "Dick Analyze"
result += "\nDick : {}".format(data["result"]["dick"])
result += "\nSize : {}".format(data["result"]["size"])
result += "\nAbility : {}".format(data["result"]["ability"])
result += "\nFlexibility : {}".format(data["result"]["flexibility"])
result += "\nDescription : {}".format(data["result"]["description"])
result += "\nPicture : {}".format(data["result"]["picture"])
print(result)

# Get JSON results
print(data)
