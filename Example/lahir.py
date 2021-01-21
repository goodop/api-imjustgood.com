from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
tgl = "17-08-1945" # example birth date
data = media.lahir(tgl)

# Get attributes
result = "Lahir : {}".formaat(data["result"]["lahir"])
result = "\nHari : {}".formaat(data["result"]["hari"])
result = "\nZodiac : {}".formaat(data["result"]["zodiak"])
result = "\nUltah : {}".formaat(data["result"]["ultah"])
result = "\nUsia : {}".formaat(data["result"]["usia"])
print(result)

# Get JSON results
print(data)
