from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
tgl = "17-08-1945" # example birth date
data = media.lahir(tgl)

# Get attributes
result = "Lahir : {}".format(data["result"]["lahir"])
result = "\nHari : {}".format(data["result"]["hari"])
result = "\nZodiac : {}".format(data["result"]["zodiak"])
result = "\nUltah : {}".format(data["result"]["ultah"])
result = "\nUsia : {}".format(data["result"]["usia"])
print(result)

# Get JSON results
print(data)
