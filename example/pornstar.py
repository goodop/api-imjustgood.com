from justgood import imjustgood
import random

api  = imjustgood("YOUR_APIKEY_HERE")
data = api.pornstar()
print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES
stars  = random.choice(data["result"])
result = "Name : {}".format(stars["pornstar"])
result += "\nBirth : {}".format(stars["birth"])
result += "\nGender : {}".format(stars["gender"])
result += "\nCountry : {}".format(stars["country"])
result += "\nHeight : {}".format(stars["height"])
if stars["gender"] == "male":
    result += "\nDick : {}".format(stars["dick"])
if stars["gender"] == "female":
    result += "\nBreast : {}".format(stars["breast"])
    result += "\nTits : {}".format(stars["tits"])
result += "\n\nImage URL :\n{}".format(stars["image"])
print(result)
