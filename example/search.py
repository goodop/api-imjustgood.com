from justgood import imjustgood

api  = imjustgood("YOUR_APIKEY_HERE")
data = api.search("mini selfbot line")
print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES
number = 0
result = "Google Result :"
for s in data["result"]:
    number += 1
    result += "\n{}. {}".format(number,s["title"])
    result += "\n{}".format(s["snippet"])
    result += "\n{}".format(s["url"])
print(result)
