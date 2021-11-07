from justgood import imjustgood

api     = imjustgood("YOUR_APIKEY_HERE")
data    = api.facebookdl("https://fb.watch/407ynrmyQq/")
print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES
result  = "Author : {}".format(data["result"]["author"])
result += "\nCaption : {}".format(data["result"]["caption"])
result += "\nVideo URL : {}".format(data["result"]["videoUrl"])
print(result)
