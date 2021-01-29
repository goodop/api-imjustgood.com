from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
url_post = "https://www.tiktok.com/@mamayukakuroyanagi/video/6810023518508518657" # example tiktok video url
data = media.tiktokdl(url_post)

# Get attributes
result = "Tiktok Downloader"
result += "\n\nUsername : {}".format(data["result"]["username"])
result += "\nFullname : {}".format(data["result"]["fullname"])
if data["result"]["private"] == True:
   private = "Enable"
else:
   private = "Disable"
result += "\nPrivate : {}".format(private)
result += "\nPlay : {}".format(data["result"]["play"])
result += "\nLike : {}".format(data["result"]["like"])
result += "\nShare : {}".format(data["result"]["share"])
result += "\nComment : {}".format(data["result"]["comment"])
result += "\nCreatetime : {}".format(data["result"]["created"])
result += "\n\nCaption : {}".format(data["result"]["description"])
result += "\n\nProfile URL : {}".format(data["result"]["profileUrl"])
result += "\n\nPost URL : {}".format(data["result"]["postUrl"])
result += "\n\nThumbnail : {}".format(data["result"]["thumbnail"])
result += "\n\nDownload URL : {}".format(data["result"]["videoUrl"])
print(result)

# Get JSON results
print(data)
