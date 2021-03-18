from justgood import imjustgood
import random

media = imjustgood("YOUR_APIKEY_HERE")
query = "coding" # example query
data = media.gif(query)

# Get attributes
result = random.choice(data["result"])
print(result)

# Get JSON results
print(data)
