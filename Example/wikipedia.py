from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
query = "jakarta" # example query
data = media.wikipedia(query)

# Get attributes
result = "Wikipedia : {}".format(query)
result += "\nDescription : {}".format(data["result"])
print(result)

# Get JSON results
print(data)
