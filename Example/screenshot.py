from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
web_url = "https://imjustgood.com/team" # example website url
data = media.screenshot(web_url)

# Get attributes
result = "Screenshot Result :"
result += "\nDekstop screen : {}".format(data["result"]["desktop"])
result += "\nMobile screen : {}".format(data["result"]["mobile"])
print(result)

# Get JSON results
print(data)
