from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
courier = "jne" # example courier express
resiNum = "CGK2H03789568816" # example resi number
data = media.resi(courier,resiNum)

# Get attributes
result = "{}\n".format(data["result"]["courier"])
result += "\nResi : {}".format(data["result"]["code"])
result += "\nStatus : {}".format(data["result"]["status"])
result += "\nJenis : {}".format(data["result"]["service"])
result += "\nBerat : {}".format(data["result"]["weight"])
result += "\nHarga : {}".format(data["result"]["price"])
result += "\nPukul : {}".format(data["result"]["time"])
result += "\nTanggal : {}".format(data["result"]["date"])
result += "\n\nDeskripsi :\n{}".format(data["result"]["desc"])
result += "\n\nPengirim :\n{} - {}".format(data["result"]["sender"]["name"],data["result"]["sender"]["city"])
result += "\n\nPenerima :\n{} - {}".format(data["result"]["receiver"]["name"],data["result"]["receiver"]["city"])
if data["result"]["timeExpress"] != []:
    for a in data["result"]["timeExpress"]:
        result += "\n\n[ {} ]".format(a["date"])
        result += "\n{}".format(a["desc"])
        if a["location"] != "":
           result += "\n{}".format(a["location"])
print(result)

# Get JSON results
print(data)
