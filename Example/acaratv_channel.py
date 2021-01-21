from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
query = "globaltv" # example tv channel
data = media.acaratv_channel(query)

# Get attributes
result = "Acara {}".format(query)
for a in data["result"]:
    result += "\n{}".format(a)
print(result)

# Get JSON results
print(data)
