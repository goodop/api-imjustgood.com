from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
city = "garut" # example city name
data = media.cinema(city)

# Get cinema attributes
result = "Cinema 21"
result += "\n\nCity : {}\n".format(data["result"]["city"])
number = 0
for a in data["result"]["data"]:
    number += 1
    result += "\n{}. {}".format(number,a["cinema"])
print(result)

# Get cinema details attributes
number = 0
select_ = 1
cinema = data["result"]["data"]
list_cinema = [o for o in cinema]
track = cinema[list_cinema[select_-1]]
result = "{}".format(track["cinema"])
result += "\n{}".format(track["address"])
result += "\n\nNow playing :"
for a in track["nowPlaying"]:
    number += 1
    result += "\n{}. {}".format(number,a["movie"])
result += "\n\nStudio Image : {}".format(track["studioImage"])
print(result)

# Get movie details attributes
number = 0
select_one = 1
select_two = 1
shotime = ""
cinema = data["result"]["data"]
list_cinema = [o for o in cinema]
track = cinema[list_cinema[select_one-1]]
list_track = [y for y in track["nowPlaying"]]
movies = list_track[select_two-1]
for x in movies["showtime"]:
    showtime += "{}, ".format(x)
result = "{}".format(movies["movie"])
result += "\n\nPrice : {}".format(movies["price"])
result += "\n\nShowtime : {}".format(showtime[:-2])
result += "\n\nGenre : {}".format(movies["genre"])
result += "\nDuration : {}".format(movies["duration"])
result += "\nDirector : {}".format(movies["director"])
result += "\nActor : {}".format(movies["actor"])
result += "\n\nSynopsis :\n{}".format(movies["synopsis"])
result += "\n\nPoster : {}".format(movies["poster"])
print(result)

# Get JSON results
print(data)
