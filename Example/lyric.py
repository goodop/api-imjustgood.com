from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
query = "crawling"
data = media.lyric(query)

result = "Lyric Finder"
result += "\nTitle : {}".format(data["result"]["title"])
result += "\nArtist : {}".format(data["result"]["artist"])
result += "\n\Lyric :\n{}".format(data["result"]["lyric"])

print(result)
