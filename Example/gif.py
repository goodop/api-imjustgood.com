from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
query = "coding" # example query
data = media.gif(query)
for gif in data["result"]:
    print(gif)
