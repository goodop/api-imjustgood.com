from justgood import imjustgood

api  = imjustgood("YOUR_APIKEY_HERE")
data = api.lyric("crawling")
print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES
result += "Title : {}".format(data["result"]["title"])
result += "\nArtist : {}".format(data["result"]["artist"])
result += "\n\Lyric :\n{}".format(data["result"]["lyric"])
print(result)
