from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
data = media.topnews()

# Get attributes
number = 0
result = "Top News Daily"
for a in data["result"]:
    number += 1
    result += "\n\n{}. {}".format(number,a["title"])
    result += "\nSource : {}".format(a["source"])
    result += "\nAuthor : {}".format(a["author"])
    result += "\nPage : {}".format(a["url"])
print(result)

# Get JSON results
print(data)
