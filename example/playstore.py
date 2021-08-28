from justgood import imjustgood

api  = imjustgood("YOUR_APIKEY_HERE")
data = api.playstore("gojek")
print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES
number = 0
result = "GOOGLE PLAYSTORE :"
for a in data["result"]:
    number += 1
    result += "\n\n{}. {}".format(number, a["title"])
    result += "\nDeveloper : {}".format(a["developer"])
    result += "\nThumbnail : {}".format(a["thumbnail"])
    result += "\nURL : {}".format(a["pageUrl"])
print(result)
