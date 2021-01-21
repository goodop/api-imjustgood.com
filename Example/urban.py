from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
query = "wtf" # example query
data = media.urban(query)

# Get attributes
result = "Urban Dictionary"
result += "\nDefinition : {}".format(data["result"]["definition"])
result += "\nExample : {}".format(data["result"]["example"])
print(result)

# Get JSON results
print(data)
