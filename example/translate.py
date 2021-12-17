from justgood import imjustgood

api     = imjustgood("YOUR_APIKEY_HERE")
data    = api.translate("id", "hasta la vista baby")
print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES
result  = "Traslated from {} ".format(data["result"]["fromLanguage"])
result += "to {}".format(data["result"]["toLanguage"])
result += "\n{}".format(data["result"]["translate"])
print(result)

# GET LANGUAGE CODE HERE
# https://api.imjustgood.com/language/code
