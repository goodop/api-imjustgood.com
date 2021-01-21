from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
query = "boruto" # example query manga
data = media.mangaSearch(query)

# Get information attributes
result = "{}".format(data["result"]["title"])
result += "\nAuthor : {}".format(data["result"]["author"])
result += "\nGenre : {}".format(data["result"]["genre"])
result += "\nRating : {}".format(data["result"]["rating"])
result += "\nRelease : {}".format(data["result"]["release"])
result += "\nStatus : {}".format(data["result"]["status"])
result += "\nType : {}".format(data["result"]["type"])
result += "\nUpdate : {}".format(data["result"]["updated"])
result += "\n\nSynopsis :\n{}".format(data["result"]["synopsis"])
result += "\n\nThumbnail : {}".format(data["result"]["thumbnail"])
print(result)

# Get list chapter attributes
result = "{}".format(data["result"]["title"])
for a in data["result"]["manga"]:
    result += "\n\nChapter {}".format(a["chapter"])
    result += "\nRelease : {}".format(a["release"])
    result += "\nChapter Id : {}".format(a["id"])
print(result)

# Get JSON results
print(data)
