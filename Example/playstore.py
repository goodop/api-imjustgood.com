from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
query = "gojek" # example query
data = media.playstore(query)

# Get attributes
number = 0
result = "Playstore :"
for a in data["result"]:
    number += 1
    result += "\n\n{}. {}".format(number, a["title"])
    result += "\nDeveloper : {}".format(a["developer"])
    result += "\nThumbnail : {}".format(a["thumbnail"])
    result += "\nURL : {}".format(a["pageUrl"])
print(result)

# Get JSON results
print(data)
