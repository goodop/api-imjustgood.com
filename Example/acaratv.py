from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
data = media.acaratv()

# Get attributes
result = "Acara Tv Saat Ini"
for a data["result"]:
    for b in a:
        result += "\n\nChannel : {}".format(b)
        for c in a[b]:
            result += "\n{}".format(c)
print(result)

# Get JSON results
print(data)
