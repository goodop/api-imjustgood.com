from justgood import imjustgood

api     = imjustgood("YOUR_APIKEY_HERE")
data    = api.movie("avengers")
print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES
result  = "Title : {}".format(data["result"]["title"])
result += "\nDuration : {}".format(data["result"]["runtime"])
result += "\nYear : {}".format(data["result"]["year"])
result += "\nRelease : {}".format(data["result"]["release"])
result += "\nDVD : {}".format(data["result"]["dvd"])
result += "\ngenre : {}".format(data["result"]["genre"])
result += "\nProduction : {}".format(data["result"]["production"])
result += "\nDirector : {}".format(data["result"]["director"])
result += "\nActors : {}".format(data["result"]["actors"])
result += "\nAwards : {}".format(data["result"]["awards"])
result += "\n\nSynopsis :\n{}".format(data["result"]["synopsis"])
result += "\n\nPoster : {}".format(data["result"]["poster"])
print(result)
