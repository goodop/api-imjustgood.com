from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
query = "avengers" # example query
data = media.movie(query)

# Get attributes
result = "Movie Review"
result += "\nTitle : {}".format(data["result"]["title"])
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

# Get JSON results
print(data)
