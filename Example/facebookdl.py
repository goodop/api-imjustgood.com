from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
url_post = "https://fb.watch/407ynrmyQq/" # example facebook post url
data = media.facebookdl(url_post)

# Get attributes
result = "Facebook Downloader"
result += "\nAuthor : {}".format(data["result"]["author"])
result += "\nCaption : {}".format(data["result"]["caption"])
result += "\nVideo URL : {}".format(data["result"]["videoUrl"])
print(result)

# Get JSON results
print(data)
