from justgood import imjustgood

api    = imjustgood("YOUR_APIKEY_HERE")
data   = api.acaratv()
print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES
result = "Acara TV"
for a data["result"]:
    for b in a:
        result += "\n\nChannel : {}".format(b)
        for c in a[b]:
            result += "\n{}".format(c)
print(result)
