from justgood import imjustgood
import random

media = imjustgood("YOUR_APIKEY_HERE")
data = media.hentai()

# Get attributes
result = random.choice(data["result"])
print(result)

# Get JSON results
print(data)
