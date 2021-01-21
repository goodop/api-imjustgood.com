from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
post_url = "https://www.smule.com/p/1998769355_3429377039"
data = media.smuledl(query)

result = "Smule Downloader"
result += "\nTitle : {}".format(data["result"]["title"])
result += "\nType : {}".format(data["result"]["type"])
result += "\n\nCaption :\n{}".format(data["result"]["caption"])
result += "\n\nThumbnail :\n{}".format(data["result"]["thumbnail"])
result += "\n\nMp3 :\n{}".format(data["result"]["mp3Url"])
if data["result"]["type"] == "video":
   result += "\n\nMp4 : {}".format(data["result"]["mp4Url"])

print(result)
