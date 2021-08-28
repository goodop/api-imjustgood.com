from justgood import imjustgood

api  = imjustgood("YOUR_APIKEY_HERE")
data = api.screenshot("https://ren.imjustgood.com/p/autobots")
print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES
result  = "Screenshot Result :"
result += "\nDesktop screen : {}".format(data["result"]["desktop"])
result += "\nMobile screen : {}".format(data["result"]["mobile"])
print(result)
