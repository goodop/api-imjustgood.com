from justgood import imjustgood

api  = imjustgood("YOUR_APIKEY_HERE")
data = api.translate("en", "mengagumkan")
print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES
result  = "Traslated to {}".format(data["result"]["language"])
result += "\n{}".format(data["result"]["translate"])
print(result)

# GET MORE LANGUAGE CODE HERE
# https://api.imjustgood.com/language/code
