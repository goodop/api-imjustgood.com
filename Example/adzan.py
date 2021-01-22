from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
city = "palembang" # example city name
data = media.adzan(city)

# Get attributes
result = "Info Waktu Sholat"
result += "\nWilayah : {}".format(data["result"]["wilayah"])
result += "\nTanggal : {}".format(data["result"]["tanggal"])
result += "\n\nImsyak : {}".format(data["result"]["adzan"]["imsyak"])
result += "\nSubuh : {}".format(data["result"]["adzan"]["subuh"])
result += "\nTerbit : {}".format(data["result"]["adzan"]["terbit"])
result += "\nDhuha : {}".format(data["result"]["adzan"]["dhuha"])
result += "\nDzuhur : {}".format(data["result"]["adzan"]["dzuhur"])
result += "\nAshar : {}".format(data["result"]["adzan"]["ashar"])
result += "\nMaghrib : {}".format(data["result"]["adzan"]["maghrib"])
result += "\nIsya : {}".format(data["result"]["adzan"]["isya"])
print(result)

# Get JSON results
print(data)
