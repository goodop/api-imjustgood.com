from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
chapter_id = "boruto-naruto-next-generations-chapter-001" # example manga chapter id
data = media.mangaChapter(chapter_id)

# Get attributes
number = 0
result = "{}".format(data["result"]["title"])
for a in data["result"]["manga"]:
    number += 1
    result += "\n{}. {}".format(number,a)
print(result)

# Get JSON results
print(data)
