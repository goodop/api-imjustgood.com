from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
city = "surabaya" # example city name
data = media.cuaca(city)

# Get attributes
result = "{}".format(data["result"]["location"])
result += "\nCuaca : {}".format(data["result"]["description"])
result += "\nSuhu : {}".format(data["result"]["temperature"])
result += "\nAngin : {}".format(data["result"]["wind"])
result += "\nKelembapan : {}".format(data["result"]["humidity"])
print(result)

# Get JSON results
print(data)
