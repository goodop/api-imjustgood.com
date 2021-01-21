from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
query = "crawling" # example query
data = media.lyric(query)

# Get attributes
result = "Lyric Finder"
result += "\nTitle : {}".format(data["result"]["title"])
result += "\nArtist : {}".format(data["result"]["artist"])
result += "\n\Lyric :\n{}".format(data["result"]["lyric"])
print(result)

# Get JSON results
print(data)
