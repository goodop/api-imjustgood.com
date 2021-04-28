from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
query = "mini selfbot line" # example query
data = media.search(query)

# Get attributes
number = 0
result = "Google Result :"
for s in data["result"]:
    number += 1
    result += "\n{}. {}".format(number,s["title"])
    result += "\n{}".format(s["url"])
print(result)

# Get JSON results
print(data)
