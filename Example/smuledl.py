from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
post_url = "https://www.smule.com/p/1998769355_3429377039" # example post url
data = media.smuledl(query)

# Get attributes
result = "Smule Downloader"
result += "\n\nTitle : {}".format(data["result"]["title"])
result += "\nType : {}".format(data["result"]["type"])
result += "\n\nCaption : {}".format(data["result"]["caption"])
if data["result"]["type"] == "video":
    result += "\n\nThumbnail : {}".format(data["result"]["thumbnail"])
    result += "\n\nVideo URL : {}".format(data["result"]["mp4Url"])
result += "\n\nAudio URL : {}".format(data["result"]["mp3Url"])
print(result)

# Get JSON results
print(data)
