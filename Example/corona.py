from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
data = media.corona()

# Get attributes
result = "DATA CORONA VIRUS"
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

# Get JSON results
print(data)
