from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
tgl = "17-08-1945" # example couple date
data = media.jadian(tgl)

# Get attributes
result = "Date : {}".format(data["result"]["date"])
result += "\n\nRelated : {}".format(data["result"]["related"])
result += "\n\nDescription : {}".format(data["result"]["description"])
print(result)

# Get JSON results
print(data)
