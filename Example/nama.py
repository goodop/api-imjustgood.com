from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
name = "imjustgood" # example name
data = media.nama(name)

# Get attributes
result = "Arti Nama"
result += "\nNama : {}".format(data["result"]["name"])
result += "\nKarakter : {}".format(data["result"]["definition"])
result += "\nDeskripsi : {}".format(data["result"]["description"])
print(result)

# Get JSON results
print(data)
