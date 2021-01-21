from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
query = "iphone12" # example query
data = media.cellular(query)

# Get attributes
number = 0
result = "Spesification Cellular"
for a in data["result"]:
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

# Get JSON results
print(data)
