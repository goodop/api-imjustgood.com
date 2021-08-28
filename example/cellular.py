from justgood import imjustgood

api  = imjustgood("YOUR_APIKEY_HERE")
data = api.cellular("iphone 12")
print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES
number = 0
result = "SEARCH RESULT :"
for a in data["result"]:
    number += 1
    result += "\n\n{}. {}".format(number,a["brands"])
    result += "\nRelease : {}".format(a["release"])
    result += "\nChipset : {}".format(a["chipset"])
    result += "\nScreen : {}".format(a["screen"])
    result += "\nBattery : {}".format(a["battery"])
    result += "\nDisplay : {}".format(a["display"])
    result += "\nRam : {}".format(a["ram"])
    result += "\nStorage : {}".format(a["storage"])
    result += "\nThumbnail : {}".format(a["thumbnail"])
    result += "\nPage : {}".format(a["pageUrl"])
print(result)
