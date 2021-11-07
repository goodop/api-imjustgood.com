from justgood import imjustgood

api         = imjustgood("YOUR_APIKEY_HERE")
data        = api.karir()
print(data)

# EXAMPLE GET CERTAIN ATTRIBUTES
result      = "Info Lowongan Kerja"
for a in data["result"]:
    number += 1
    result += "\n\n{}. {}".format(number,a["perusahaan"])
    result += "\nLokasi : {}".format(a["lokasi"])
    result += "\nProfesi : {}".format(a["profesi"])
    result += "\nBagian : {}".format(a["bagian"])
    result += "\nJabatan : {}".format(a["jabatan"])
    result += "\nGaji : {}".format(a["gaji"])
    result += "\nPendidikan : {}".format(a["pendidikan"])
    result += "\nPenngalaman : {}".format(a["penngalman"])
    result += "\nSyarat : {}".format(a["syarat"])
    result += "\nDeskirpsi : {}".format(a["deskripsi"])
    result += "\nSumber : {}".format(a["sumber"])
print(result)
