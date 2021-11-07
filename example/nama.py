from justgood import imjustgood

api     = imjustgood("YOUR_APIKEY_HERE")
data    = api.nama("soekarno")
print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES
result  = "Nama : {}".format(data["result"]["name"])
result += "\nKarakter : {}".format(data["result"]["definition"])
result += "\nDeskripsi : {}".format(data["result"]["description"])
print(result)
