import json, requests, threading

class imjustgood(threading.Thread):
    def __init__(self, apikey):
        super(imjustgood, self).__init__()
        self.host = "https://api.imjustgood.com"
        self.headers = {"apikey": apikey}
        self.session = requests.Session()

    def PrintJson(self, jhon):
        print(json.dumps(jhon, indent=4, sort_keys=True))

    def Get(self, data, headers=None):
        if headers:
            headers = {**headers, **self.headers}
        else:
            headers = self.headers
        try:  
            req = json.loads(self.session.get(self.host+data,headers=headers).text)
        except:
            raise Exception("Under Maintenance.")
        if req["status"] != 200:
            raise Exception(str(req))
        return req

    def Post(self, path, headers=None, data=None, files=None, jhon=None):
        if headers:
            headers = {**headers, **self.headers}
        else:
            headers = self.headers
        try:
            req = json.loads(self.session.post(self.host+path,headers=headers,data=data,files=files,json=jhon).text)
        except:
            raise Exception("Under Maintenance.")
        if req["status"] != 200:
            raise Exception(str(req))
        return req

    def cinema(self, city):
        return self.Get("/cinema="+city)

    def youtube(self, query):
        return self.Get("/youtube="+query)

    def youtubedl(self, url):
        return self.Get("/youtubedl="+url)

    def twitter(self, userID):
        return self.Get("/twitter="+userID)

    def zodiac(self, sign):
        return self.Get("/zodiac="+sign)

    def image(self, query):
        return self.Get("/image="+query)

    def nama(self, name):
        return self.Get("/nama="+name)

    def mimpi(self, query):
        return self.Get("/mimpi="+query)

    def wallpaper(self, query):
        return self.Get("/wallpaper="+query)

    def tinyurl(self, url):
        return self.Get("/tinyurl="+url)

    def bitly(self, url):
        return self.Get("/bitly="+url)

    def porn(self, query):
        return self.Get("/porn="+query)

    def pornstar(self):
        return self.Get("/pornstar")

    def hentai(self):
        return self.Get("/hentai")

    def topnews(self):
        return self.Get("/topnews")

    def corona(self):
        return self.Get("/corona")

    def calc(self, digit):
        return self.Get("/calc="+digit)

    def wikipedia(self, query):
        return self.Get("/wikipedia="+query)

    def urban(self, query):
        return self.Get("/urban="+query)

    def movie(self, title):
        return self.Get("/movie="+title)

    def github(self, userID):
        return self.Get("/github="+userID)
    
    def joox(self, query):
        return self.Get("/joox="+query)
    
    def lyric(self, query):
        return self.Get("/lyric="+query)
    
    def smule(self, userID):
        return self.Get("/smule="+userID)
    
    def smuledl(self, link):
        return self.Get("/smuledl="+link)
    
    def tiktok(self, userID):
        return self.Get("/tiktok="+userID)
    
    def smuledl(self, link):
        return self.Get("/tiktokdl="+link)
    
    def instagram(self, userID):
        return self.Get("/instagram="+userID)
    
    def instastory(self, userID):
        return self.Get("/instastory="+userID)
    
    def instapost(self, link):
        return self.Get("/instapost="+link)
    
    def twitter(self, userID):
        return self.Get("/twitter="+userID)
    
    def playstore(self, query):
        return self.Get("/playstore="+query)

    def translate(self, lang, query):
        return self.Get("/translate/"+lang+"="+query)

    def karir(self):
        return self.Get("/karir")

    def infoHp(self, query):
        return self.Get("/cell="+query)

    def infoTanggalLahir(self, birth):
        return self.Get("/lahir="+birth)

    def infoTanggalJadian(self, love):
        return self.Get("/jadian="+love)

    def kamasutra(self):
        return self.Get("/kamasutra")

    def dick(self):
        return self.Get("/dick")

    def tits(self):
        return self.Get("/tits")

    def vagina(self):
        return self.Get("/vagina")

    def quotes(self):
        return self.Get("/quotes")

    def movie(self, query):
        return self.Get("/movie="+query)

    def bmkg(self):
        return self.Get("/bmkg")

    def acaratv(self):
        return self.Get("/acaratv/now")

    def acaraTvChannel(self, channel):
        return self.Get("/acaratv="+channel)

    def cctvCode(self):
        return self.Get("/cctv/code")

    def cctvSearch(self, code):
        return self.Get("/cctv/search/id="+code)

    def adzan(self, city):
        return self.Get("/adzan="+city)

    def cuaca(self, city):
        return self.Get("/cuaca="+city)

    def meme(self, text1, text2, urlImage):
        return self.Get("/meme/"+text1+"/"+text2+"/"+"url="+urlImage)

############# S E M P L E #################
# from justgood import imjustgood
# media = imjustgood("YOUR_APIKEY")
# data = media.cinema("jakarta")
# print(data)
