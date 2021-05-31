import json, requests, threading

class imjustgood(threading.Thread):
    def __init__(self, apikey):
        super(imjustgood, self).__init__()
        self.host = "https://api.imjustgood.com"
        self.headers = {
            "apikey": apikey,
            "User-Agent": "Justgood/5.0"
        }
        self.session = requests.Session()

    def GoodJson(self, data):
        return f"{json.dumps(data, indent=4, sort_keys=True)}"

    def Get(self, path, headers=None):
        if headers:
            headers = {**headers, **self.headers}
        else:
            headers = self.headers
        req = json.loads(self.session.get(self.host+path,headers=headers).text)
        if req["status"] != 200:
           raise Exception(req["message"])
        return req

    def Post(self, path, headers=None, data=None, files=None, jhon=None):
        if headers:
            headers = {**headers, **self.headers}
        else:
            headers = self.headers
        req = json.loads(self.session.post(self.host+path,headers=headers,data=data,files=files,json=jhon).text)
        if req["status"] != 200:
           raise Exception(req["message"])
        return req

    def youtube(self, query):
        return self.Get("/youtube="+query)

    def youtubedl(self, url):
        return self.Get("/youtubedl="+url)

    def joox(self, query):
        return self.Get("/joox="+query)
    
    def lyric(self, query):
        return self.Get("/lyric="+query)

    def smule(self, userId):
        return self.Get("/smule="+userId)
    
    def smuledl(self, url):
        return self.Get("/smuledl="+url)

    def tiktok(self, userId):
        return self.Get("/tiktok="+userId)
    
    def tiktokdl(self, url):
        return self.Get("/tiktokdl="+url)

    def instagram(self, userId):
        return self.Get("/instagram="+userId)
    
    def instapost(self, url):
        return self.Get("/instapost="+url)

    def instastory(self, userId):
        return self.Get("/instastory="+userId)

    def twitter(self, userId):
        return self.Get("/twitter="+userId)

    def twitterdl(self, url):
        return self.Get("/twitter/video?url="+url)

    def facebookdl(self, url):
        return self.Get("/facebook/video?url="+url)

    def github(self, userId):
        return self.Get("/github="+userId)

    def playstore(self, query):
        return self.Get("/playstore="+query)

    def translate(self, lang, text):
        return self.Get("/translate/"+lang+"="+text)

    def image(self, query):
        return self.Get("/image="+query)

    def wallpaper(self, query):
        return self.Get("/wallpaper="+query)

    def porn(self, query):
        return self.Get("/porn="+query)

    def pornstar(self):
        return self.Get("/pornstar")

    def hentai(self):
        return self.Get("/hentai")

    def kamasutra(self):
        return self.Get("/kamasutra")

    def dick(self):
        return self.Get("/dick")

    def tits(self):
        return self.Get("/tits")

    def vagina(self):
        return self.Get("/vagina")

    def meme(self, text1, text2, imageUrl):
        return self.Get("/meme/"+text1+"/"+text2+"/url="+imageUrl)

    def movie(self, query):
        return self.Get("/movie="+query)

    def movie_quotes(self):
        return self.Get("/movie/quotes")

    def cinema(self, city):
        return self.Get("/cinema="+city)

    def tinyurl(self, url):
        return self.Get("/tinyurl="+url)

    def bitly(self, url):
        return self.Get("/bitly="+url)

    def kbbi(self, query):
        return self.Get("/kbbi="+query)

    def topnews(self):
        return self.Get("/topnews")

    def wikipedia(self, query):
        return self.Get("/wikipedia="+query)

    def urban(self, query):
        return self.Get("/urban="+query)

    def zodiac(self, sign):
        return self.Get("/zodiac="+sign)

    def adzan(self, city):
        return self.Get("/adzan="+city)

    def cuaca(self, city):
        return self.Get("/cuaca="+city)

    def bmkg(self):
        return self.Get("/bmkg")

    def corona(self):
        return self.Get("/corona")

    def karir(self):
        return self.Get("/karir")
 
    def cellular(self, query):
        return self.Get("/cell="+query)

    def lahir(self, date):
        return self.Get("/lahir="+date)

    def jadian(self, date):
        return self.Get("/jadian="+date)
 
    def nama(self, name):
        return self.Get("/nama="+name)

    def mimpi(self, query):
        return self.Get("/mimpi="+query)

    def acaratv(self):
        return self.Get("/acaratv/now")

    def acaratv_channel(self, channel):
        return self.Get("/acaratv="+channel)

    def cctv_code(self):
        return self.Get("/cctv/code")

    def cctvSearch(self, code):
        return self.Get("/cctv/search/id="+code)

    def mangaSearch(self, query):
        return self.Get("/manga/search="+query)

    def mangaChapter(self, chapterId):
        return self.Get("/manga/chapter="+chapterId)

    def timeline(self, url):
        return self.Get("/timeline="+url)

    def resi(self, query, code):
        return self.Get("/resi/"+query+"="+code)

    def screenshot(self, url):
        return self.Get("/screenshot?url="+url)

    def imgurl(self, path):
        return self.Post("/imgurl",files={"file": open(path,"rb")})

    def gif(self, query):
        return self.Get("/gif="+query)

    def search(self, query):
        return self.Get("/search="+query)

    def calc(self, query):
        return self.Get("/calc="+query)

    def language(self):
        return self.Get("/language/code")

    def lineapp(self):
        return self.Get("/line")

    def check_ip(self, query):
        return self.Get("/ip="+query)

    def BinaryEncode(self, query):
        return self.Get("/binary/text?q="+query)

    def BinaryDecode(self, query):
        return self.Get("/binary/digit?q="+query)

    def B64Encode(self, query):
        return self.Get("/base64/text?q="+query)

    def B64Decode(self, query):
        return self.Get("/base64/code?q="+query)

    def fancy(self, query):
        return self.Get("/fancy?text="+query)

    def simisimi(self, query):
        return self.Get("/simisimi?text="+query)

    def imagetext(self, query):
        return self.Get("/imgtext?text="+query)

    def ascii(self,query):
        main = self.session.get(self.host+"/ascii="+query,headers=self.headers)
        return main.text.split("pre")[1][1:-2]

    def customlink(self, label, url):
        return self.Get("/custom/make", headers={"label": label, "url": url})

    def watermark_image(self, imageUrl, iconUrl):
        return self.Get("/watermark/image?image="+imageUrl+"&icon="+iconUrl)

    def watermark_text(self, imageUrl, text):
        return self.Get("/watermark/text?image="+imageUrl+"&text="+text)
