from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
courier = "jne" # example courier express
resiNum = "CGK2H03789568816" # example resi number
data = media.resi(courier,resiNum)

# Get attributes
result = "Info Pengiriman\n"
result += "\nResi : {}".format(data["result"]["code"])
result += "\nExpress : {}".format(data["result"]["courier"])
result += "\nType : {}".format(data["result"]["service"])
result += "\nStatus : {}".format(data["result"]["status"])
result += "\nHarga : {}".format(data["result"]["price"])
result += "\nBerat : {}".format(data["result"]["weight"])
result += "\nTanggal : {}".format(data["result"]["date"])
result += "\nPukul : {}".format(data["result"]["time"])
result += "\n\nDeskripsi :\n{}, {}".format(data["result"]["desc"])
result += "\n\nPengirim :\n{}, {}".format(data["result"]["sender"]["name"],data["result"]["sender"]["city"])
result += "\n\nPenerima :\n{}, {}\n\n".format(data["result"]["receiver"]["name"],data["result"]["receiver"]["city"])
result += "Riwayat Pengiriman :"
for a in data["result"]["timeExpress"]:
    result += "\n[{}] {}".format(a["date"],a["desc"])
    if a["location"] != "":
       result += "\n{}\n".format(a["location"])
print(result)

# Get JSON results
print(data)
