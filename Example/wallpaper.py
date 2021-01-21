from justgood import imjustgood
import random

media = imjustgood("YOUR_APIKEY_HERE")
query = "nude" # example query
data = media.wallpaper(query)

# Get attributes
list_wallpaper = data["result"]
result = random.choice(list_wallpaper)
print(result)

# Get JSON results
print(data)
