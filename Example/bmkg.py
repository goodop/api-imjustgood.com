from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
data = media.bmkg()

# Get attributes
result = "Info Gempa BMKG"
result += "\nTanggal : {}".format(data["result"]["tanggal"])
result += "\nPukul : {}".format(data["result"]["pukul"])
result += "\nLokasi : {}".format(data["result"]["lokasi"])
result += "\nWilayah : {}".format(data["result"]["wilayah"])
result += "\nKordinat : {}".format(data["result"]["kordinat"])
result += "\nKedalaman : {}".format(data["result"]["kedalaman"])
result += "\nKekuatan : {}".format(data["result"]["kekuatan"])
result += "\nArahan : {}".format(data["result"]["arahan"])
result += "\nSaran : {}".format(data["result"]["saran"])
result += "\nPeta Skema : {}".format(data["result"]["skema"])
print(result)

# Get JSON results
print(data)
