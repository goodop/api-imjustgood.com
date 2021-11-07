from justgood import imjustgood

api     = imjustgood("YOUR_APIKEY_HERE")
data    = api.mangaSearch("boruto")
print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES
result  = "{}".format(data["result"]["title"])
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
