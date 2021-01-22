from justgood import imjustgood
import random

media = imjustgood("YOUR_APIKEY_HERE")
data = media.pornstar()

# Get attributes
stars = random.choice(data["result"])
result = "Pornstar"
result += "\nName : {}".format(stars["pornstar"])
result += "\nBirth : {}".format(stars["birth"])
result += "\nCountry : {}".format(stars["country"])
result += "\nHeight : {}".format(stars["height"])
result += "\nBreast : {}".format(stars["breast"])
result += "\nTits : {}".format(stars["tits"])
result += "\n\nImage URL :\n{}".format(stars["image"])
print(result)

# Get JSON results
print(data)
