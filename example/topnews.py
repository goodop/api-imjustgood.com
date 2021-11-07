from justgood import imjustgood

api    = imjustgood("YOUR_APIKEY_HERE")
data   = api.topnews()
print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES
number = 0
result = "Daily Top News"
for a in data["result"]:
    number += 1
    result += "\n\n{}. {}".format(number,a["title"])
    result += "\nSource : {}".format(a["source"])
    result += "\nAuthor : {}".format(a["author"])
    result += "\nPage : {}".format(a["url"])
print(result)
