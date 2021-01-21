from justgood import imjustgood
import random

media = imjustgood("YOUR_APIKEY_HERE")
query = "teacher" # example query
data = media.image(query)

# Get attributes
list_image = data["result"]
result = random.choice(list_image)
print(result)

# Get JSON results
print(data)
