from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
query = "ciuman" # example query
data = media.mimpi(query)

# Get attributes
result = "Arti Mimpi"
for a in data["result"]:
    result += "\n\nMimpi : {}".format(a["dream"])
    result += "\nArti : {}".format(a["meaning"])
print(result)

# Get JSON results
print(data)
