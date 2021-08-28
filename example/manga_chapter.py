from justgood import imjustgood

api  = imjustgood("YOUR_APIKEY_HERE")
data = api.mangaChapter("boruto-naruto-next-generations-chapter-001")
print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES
number = 0
result = "{}".format(data["result"]["title"])
for a in data["result"]["manga"]:
    number += 1
    result += "\n{}. {}".format(number,a)
print(result)
