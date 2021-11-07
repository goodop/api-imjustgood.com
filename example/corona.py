from justgood import imjustgood

api     = imjustgood("YOUR_APIKEY_HERE")
data    = api.corona()
print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES
result  = "CORONA VIRUS QUICKCOUNT"
result += "\n{}".format(data["result"]["date"])
result += "\n\nWorld"
result += "\nCase : {}".format(data["result"]["world"]["case"])
result += "\nFit : {}".format(data["result"]["world"]["fit"])
result += "\nRip : {}".format(data["result"]["world"]["rip"])
result += "\n\nIndonesia"
result += "\nCase : {}".format(data["result"]["indonesia"]["case"])
result += "\nFit : {}".format(data["result"]["indonesia"]["fit"])
result += "\nRip : {}".format(data["result"]["indonesia"]["rip"])
print(result)
