from justgood import imjustgood

api  = imjustgood("YOUR_APIKEY_HERE")
data = api.urban("dick head")
print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES
result  = "Urban Dictionary"
result += "\nDefinition : {}".format(data["result"]["definition"])
result += "\nExample : {}".format(data["result"]["example"])
print(result)
