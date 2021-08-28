from justgood import imjustgood

api  = imjustgood("YOUR_APIKEY_HERE")
data = api.dick()
print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES
result  = "Dick : {}".format(data["result"]["dick"])
result += "\nSize : {}".format(data["result"]["size"])
result += "\nAbility : {}".format(data["result"]["ability"])
result += "\nFlexibility : {}".format(data["result"]["flexibility"])
result += "\nDescription : {}".format(data["result"]["description"])
result += "\nPicture : {}".format(data["result"]["picture"])
print(result)
