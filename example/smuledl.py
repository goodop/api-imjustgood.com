from justgood import imjustgood

api     = imjustgood("YOUR_APIKEY_HERE")
data    = api.smuledl("https://www.smule.com/p/1998769355_3429377039")
print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES
result  = "Title : {}".format(data["result"]["title"])
result += "\nType : {}".format(data["result"]["type"])
result += "\n\nCaption : {}".format(data["result"]["caption"])
if data["result"]["type"] == "video":
    result += "\n\nThumbnail : {}".format(data["result"]["thumbnail"])
    result += "\n\nVideo URL : {}".format(data["result"]["mp4Url"])
result += "\n\nAudio URL : {}".format(data["result"]["mp3Url"])
print(result)
