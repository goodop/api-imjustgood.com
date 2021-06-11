from justgood import imjustgood
from requests import get
import json, time, random

''' 
JUST EXAMPLE TO MAKE EASY GET API ATTRIBUTES
contact us here https://imjustgood.com/team
'''

key = "Your_Apikey_Here"
api = imjustgood(key)

# APIKEY STATUS
data = api.status()
result = "ID : {}".format(data["result"]["id"])
result += "\nType : {}".format(data["result"]["type"])
result += "\nUsage : {}".format(data["result"]["usage"])
result += "\nExpired : {}".format(data["result"]["expired"])
result += "\nRestart : {}".format(data["result"]["restart"])
result += "\nTimeleft : {}".format(data["result"]["timeleft"])
print(result)

# YOUTUBE DOWNLOADER BY TITLE
data = api.youtube("despacito")
result = "Title : {}".format(data["result"]["title"])
result += "\nAuthor : {}".format(data["result"]["author"])
result += "\nDuration : {}".format(data["result"]["duration"])
result += "\nWatched : {}".format(data["result"]["watched"])
result += "\n\nThumbnail :\n{}".format(data["result"]["thumbnail"])
result += "\n\nAudio :\n{}".format(data["result"]["audioUrl"])
result += "\n\nVideo :\n{}".format(data["result"]["videoUrl"])
result += "\n\nPage : {}".format(data["result"]["pageUrl"])
print(result)

# YOUTUBE DOWNLOADER BY URL
data = api.youtubedl("https://youtu.be/kJQP7kiw5Fk")
result = "Title : {}".format(data["result"]["title"])
result += "\nAuthor : {}".format(data["result"]["author"])
result += "\nDuration : {}".format(data["result"]["duration"])
result += "\nWatched : {}".format(data["result"]["watched"])
result += "\n\nThumbnail :\n{}".format(data["result"]["thumbnail"])
result += "\n\nAudio :\n{}".format(data["result"]["audioUrl"])
result += "\n\nVideo :\n{}".format(data["result"]["videoUrl"])
result += "\n\nPage : {}".format(data["result"]["pageUrl"])
print(result)

# JOOX DOWNLOADER
data = api.joox("lathi")
result = "Singer : {}".format(data["result"]["singer"])
result += "\nTitle : {}".format(data["result"]["title"])
result += "\nDuration : {}".format(data["result"]["duration"])
result += "\nSize : {}".format(data["result"]["size"])
result += "\n\nThumbnail :\n{}".format(data["result"]["thumbnail"])
result += "\n\nMp3 :\n{}".format(data["result"]["mp3Url"])
print(result)

# LYRIC FINDER
data = api.lyric("crawling")
result += "Title : {}".format(data["result"]["title"])
result += "\nArtist : {}".format(data["result"]["artist"])
result += "\n\Lyric :\n{}".format(data["result"]["lyric"])
print(result)

# SMULE PROFILE
data = api.smule("avamax")
result = "Account Id : {}".format(data["result"]["accountId"])
result += "\nUsername : {}".format(data["result"]["username"])
result += "\nFullname : {}".format(data["result"]["fullname"])
result += "\nBiography : {}".format(data["result"]["biography"])
result += "\nLocation : {}".format(data["result"]["location"])
result += "\nFollowers : {}".format(data["result"]["followers"])
result += "\nFollowing : {}".format(data["result"]["following"])
result += "\nRecording : {}".format(data["result"]["recording"])
result += "\nVIP : {}".format(data["result"]["vip"])
result += "\nVerified : {}".format(data["result"]["verified"])
result += "\nProfile URL : {}".format(data["result"]["profileUrl"])
result += "\nPicture URL : {}".format(data["result"]["pictureUrl"])
if data["result"]["lastpost"] != []:
    number = 0
    result += "\n\nLastpost :"
    for i in data["result"]["lastpost"]:
        number += 1
        result += "\n  {}. {}".format(number,i["title"])
print(result)

# SMULE LAST PERFORMANCES
data = api.smule("avamax")
postcount = 1 # count number of last performances
lastpost = data["result"]["lastpost"][postcount-1]
result = "Title : {}".format(lastpost["title"])
result += "\nArtist : {}".format(lastpost["artist"])
result += "\nType : {}".format(lastpost["type"])
result += "\nCollabs : {}".format(lastpost["performances"])
result += "\nCreated : {}".format(lastpost["created"])
result += "\nListens : {}".format(lastpost["listens"])
result += "\nLoves : {}".format(lastpost["loves"])
result += "\nGifts : {}".format(lastpost["gifts"])
result += "\nComments : {}".format(lastpost["comments"])
result += "\nCaption :\n{}".format(lastpost["caption"])
if lastpost["type"] == "video":
    result += "\nThumbnail : {}".format(lastpost["thumbnail"])
    result += "\nVideo URL :\n{}".format(lastpost["videoUrl"])
result += "\nAudio URL :\n{}".format(lastpost["audioUrl"])
print(result)

# SMULE DOWNLOADER BY URL
data = api.smuledl("https://www.smule.com/p/1998769355_3429377039")
result = "Title : {}".format(data["result"]["title"])
result += "\nType : {}".format(data["result"]["type"])
result += "\n\nCaption : {}".format(data["result"]["caption"])
if data["result"]["type"] == "video":
    result += "\n\nThumbnail : {}".format(data["result"]["thumbnail"])
    result += "\n\nVideo URL : {}".format(data["result"]["mp4Url"])
result += "\n\nAudio URL : {}".format(data["result"]["mp3Url"])
print(result)

# TIKTOK PROFILE
data = api.tiktok(userId)
result = "Username : {}".format(data["result"]["username"])
result += "\nFullname : {}".format(data["result"]["fullname"])
result += "\nBiography : {}".format(data["result"]["biography"])
result += "\nFollowers : {}".format(data["result"]["followers"])
result += "\nFollowing : {}".format(data["result"]["following"])
result += "\nLikes : {}".format(data["result"]["likes"])
result += "\nVideos : {}".format(data["result"]["videos"])
result += "\n\nProfile : {}".format(data["result"]["profileUrl"])
result += "\n\nPicture : {}".format(data["result"]["pictureUrl"])
result += "\n\nLastpost :"
result += "\n- Page : {}".format(data["result"]["lastpost"]["pageUrl"])
result += "\n- Poster : {}".format(data["result"]["lastpost"]["poster"])
result += "\n- Video : {}".format(data["result"]["lastpost"]["videoUrl"])
print(result)

# TIKTOK DOWNLOADER BY URL
data = api.tiktokdl("https://www.tiktok.com/@mamayukakuroyanagi/video/6810023518508518657")
result = "Thumbnail : {}".format(data["result"]["thumbnail"])
result += "\nWatermark : {}".format(data["result"]["watermark"])
result += "\nNo watermark : {}".format(data["result"]["no_watermark"])
print(result)

# INSTAGRAM PROFILE
data = api.instagram("the.autobots_corp")
result = "nUsername : {}".format(data["result"]["id"])
result += "\nUsername : {}".format(data["result"]["username"])
result += "\nFullname : {}".format(data["result"]["fullname"])
result += "\nBiography : {}".format(data["result"]["biography"])
result += "\nWebsite : {}".format(data["result"]["website"])
result += "\nPrivate : {}".format(data["result"]["private"])
result += "\nVerified : {}".format(data["result"]["verified"])
result += "\nPost : {}".format(data["result"]["post"])
result += "\nFollower : {}".format(data["result"]["follower"])
result += "\nFollowing : {}".format(data["result"]["following"])
result += "\n\nPicture :\n{}".format(data["result"]["picture"])
result += "\n\nProfile :\n{}".format(data["result"]["profile"])
if data["result"]["lastpost"] != []:
    number = 0
    result += "\n\nLastpost"
    for a in data["result"]["lastpost"]:
        number += 1
        result += "\n{}. {}".format(number, a["caption"])
        result += "\n{}".format(a["url"])
        result += "\n   Like : {}".format(number, a["like"])
        result += "\n   Comment : {}".format(number, a["comment"])
        result += "\n   Created : {}".format(a["created"])
        result += "\n   PageUrl : {}".format(a["page"])
print(result)

# INSTAGRAM POST DOWNLOADER BY URL
data = api.instapost("https://www.instagram.com/p/COjHqwGhFA6/")
result = "Username : {}".format(data["result"]["username"])
result += "\nFullname : {}".format(data["result"]["fullname"])
result += "\nCreated : {}".format(data["result"]["created"])
result += "\nCaption : {}".format(data["result"]["caption"])
result += "\nLikes : {}".format(data["result"]["likes"])
result += "\n\nPicture :\n{}".format(data["result"]["picture"])
number = 0
result += "\n\nMedia Post"
for a in data["result"]["postData"]:
    number += 1
    if a["type"] == "image":
       result += "\n{}. Image Url : {}".format(number, a["postUrl"])
    if a["type"] == "video":
       result += "\n{}. Video Url : {}".format(number, a["postUrl"])
       result += "\nPoster Url: {}".format(a["poster"])
print(result)

# INSTAGRAM STORIES
data = api.instastory("the.goperation")
result = "Id : {}".format(data["result"]["id"])
result += "\nFullname : {}".format(data["result"]["fullname"])
result += "\nUsername : {}\n".format(data["result"]["username"])
result += "\nPicture : {}\n".format(data["result"]["picture"])
result += "\nProfile : {}\n".format(data["result"]["profile"])
result += "\n- List stories -"
number = 0
for a in data["result"]["stories"]:
  number += 1
  result += "\nStories {} : {}".format(number,a["url"])
  result += "\nCreated {}".format(a["created"])
  if a["type"] == "video":
    result += "\Thumbnail : {}".format(a["thumbnail"])
print(result)

# TWITTER PROFILE
data = api.twitter("rendytr_")
result = "Username : {}".format(data["result"]["username"])
result += "\nFullname : {}".format(data["result"]["fullname"])
result += "\nBiography : {}".format(data["result"]["biography"])
result += "\nTweet : {}".format(data["result"]["tweet"])
result += "\nFollower : {}".format(data["result"]["follower"])
result += "\nFollowing : {}".format(data["result"]["following"])
result += "\n\nAvatar :\n{}".format(data["result"]["avatar"])
result += "\n\nBanner :\n{}".format(data["result"]["banner"])
print(result)

# TWITTER DOWNLOADER BY URL
data = api.twitterdl("https://twitter.com/rendytr_/status/1367319659741990912?s=20")
result = "Video URL : {}".format(data["result"]["videoUrl"])
print(result)

# FACEBOOK DOWNLOADER BY URL
data = api.facebookdl("https://fb.watch/407ynrmyQq/")
result = "Author : {}".format(data["result"]["author"])
result += "\nCaption : {}".format(data["result"]["caption"])
result += "\nVideo URL : {}".format(data["result"]["videoUrl"])
print(result)

# GITHUB PROFILE
data = api.github("goodop")
result = "ID : {}".format(data["result"]["id"])
result += "\nType : {}".format(data["result"]["type"])
result += "\nUsername : {}".format(data["result"]["username"])
result += "\nFullname : {}".format(data["result"]["fullname"])
result += "\nBiography : {}".format(data["result"]["biography"])
result += "\nBlog : {}".format(data["result"]["blog"])
result += "\nEmail : {}".format(data["result"]["email"])
result += "\nCompany : {}".format(data["result"]["company"])
result += "\nCreated : {}".format(data["result"]["created_at"])
result += "\nUpdated : {}".format(data["result"]["updated_at"])
result += "\nLocation : {}".format(data["result"]["location"])
result += "\nRepositories : {}".format(data["result"]["repositories"])
result += "\nFollower : {}".format(data["result"]["follower"])
result += "\nFollowing : {}".format(data["result"]["following"])
result += "\nProfile : {}".format(data["result"]["page"])
result += "\nAvatar : {}".format(data["result"]["avatar"])
print(result)

# LINE SECONDARY LOGIN
data = api.lineqr(appName="CHROMEOS\t2.4.5\tChromeOS\t1", sysName="JUSTGOOD", cert=None)
cbpin = data["result"]["callback"]["pin"]
cbaut = data["result"]["callback"]["token"]
linkqr = data["result"]["qr"]
print(linkqr)
data = api.lineqrGetPin(cbpin)
if data["status"] == 200:
    pin = data["result"]["pin"]
    print(pin)
data = api.lineqrGetToken(cbaut)
result = "Certified : {}\n\n".format(data["result"]["cert"])
result += "Authtoken : {}".format(data["result"]["token"])
print(result)

# LINE TIMELINE DOWNLOADER BY URL
data = api.timeline("https://timeline.line.me/post/_dYzCumD5eS8O1hq9aFKBaFHwN6dX80SeSE06k6U/1150542613404018340")
result = "Display name : {}".format(data["result"]["displayName"])
result += "\nLike : {}".format(data["result"]["like"])
result += "\nShare : {}".format(data["result"]["share"])
result += "\n\nCaption : {}".format(data["result"]["caption"])
result += "\n\nPicture :\n{}".format(data["result"]["pictureUrl"])
if data["result"]["timeline"] != []:
   number = 0
   result += "\n\nMedia Post :"
   for a in data["result"]["timeline"]:
       number += 1
       if a["type"] == "image":
          result += "\n{}. {}".format(number,a["url"])
       if a["type"] == "video":
          result += "\n{}. {}".format(number,a["url"])
          result += "\nThumbnail : {}".format(a["thumbnail"])
print(result)

# LINE APP VERSION
data = api.lineapp()
result = "LINE APP VERSION"
for a in data["result"]:
    result += "\n{} : {}".format(a,data["result"][a])
print(result)

# GOOGLE SEARCH
data = api.search("mini selfbot line")
number = 0
result = "Google Result :"
for s in data["result"]:
    number += 1
    result += "\n{}. {}".format(number,s["title"])
    result += "\n{}".format(s["url"])
print(result)

# GOOGLE IMAGE
data = api.image("teacher")
list_image = data["result"]
result = random.choice(list_image)
print(result)

# GOOGLE PLAYSTORE
data = api.playstore("gojek")
number = 0
result = "Google Playstore"
for a in data["result"]:
    number += 1
    result += "\n\n{}. {}".format(number, a["title"])
    result += "\nDeveloper : {}".format(a["developer"])
    result += "\nThumbnail : {}".format(a["thumbnail"])
    result += "\nURL : {}".format(a["pageUrl"])
print(result)

# GOOGLE TRANSLATE
''' check more language code here
https://api.imjustgood.com/language/code '''
data = api.translate("en", "mengagumkan")
result = data["result"]["translate"]
print(result)

# LANGUAGE CODE
data = api.language()
result = "Language Code :"
for a in data:
    result += "\n{}".format(a)
print(result)

# WALLPAPER - PIXABAY
data = api.wallpaper("nude")
list_wallpaper = data["result"]
result = random.choice(list_wallpaper)
print(result)

# PORN VIDEOS
data = api.porn("blonde")
result = "Title : {}".format(data["result"]["title"])
result += "\nDuration : {}".format(data["result"]["duration"])
result += "\nQuality : {}".format(data["result"]["quality"])
result += "\nWatched : {}".format(data["result"]["watched"])
result += "\n\nThumbnail :\n{}".format(data["result"]["thumbnail"])
result += "\n\nVideo URL :\n{}".format(data["result"]["videoUrl"])
print(result)

# PORNSTAR
data = api.pornstar()
stars = random.choice(data["result"])
result = "Name : {}".format(stars["pornstar"])
result += "\nBirth : {}".format(stars["birth"])
result += "\nGender : {}".format(stars["gender"])
result += "\nCountry : {}".format(stars["country"])
result += "\nHeight : {}".format(stars["height"])
if stars["gender"] == "male":
    result += "\nDick : {}".format(stars["dick"])
if stars["gender"] == "female":
    result += "\nBreast : {}".format(stars["breast"])
    result += "\nTits : {}".format(stars["tits"])
result += "\n\nImage URL :\n{}".format(stars["image"])
print(result)

# HENTAI
data = api.hentai()
result = random.choice(data["result"])
print(result)

# KAMASUTRA
data = api.kamasutra()
result = "Style : {}".format(data["result"]["style"])
result += "\nDescription :\n{}".format(data["result"]["description"])
result += "\nPicture : {}".format(data["result"]["thumbnail"])
print(result)

# DICK ANALYZE
data = api.dick()
result = "Dick : {}".format(data["result"]["dick"])
result += "\nSize : {}".format(data["result"]["size"])
result += "\nAbility : {}".format(data["result"]["ability"])
result += "\nFlexibility : {}".format(data["result"]["flexibility"])
result += "\nDescription : {}".format(data["result"]["description"])
result += "\nPicture : {}".format(data["result"]["picture"])
print(result)

# VAGINA ANALYZE
data = api.vagina()
result = "Vagina : {}".format(data["result"]["vagina"])
result += "\nDepth : {}".format(data["result"]["depth"])
result += "\nGrip : {}".format(data["result"]["grip"])
result += "\nHumidity : {}".format(data["result"]["humidity"])
result += "\nElasticity : {}".format(data["result"]["elasticity"])
result += "\nDescription : {}".format(data["result"]["description"])
result += "\nPicture : {}".format(data["result"]["picture"])
print(result)

# TITS ANALYZE
data = api.tits()
result = "Tits : {}".format(data["result"]["tits"])
result += "\nSize : {}{}".format(data["result"]["size"],data["result"]["cup"])
result += "\nNipple : {}".format(data["result"]["nipple"])
result += "\nAerola : {}".format(data["result"]["aerola"])
result += "\nDescription : {}".format(data["result"]["description"])
result += "\nPicture : {}".format(data["result"]["picture"])
print(result)

# MEME GENERATE
text1 = "top"
text2 = "bottom"
imageUrl = "http://www.gstatic.com/webp/gallery/1.png"
data = api.meme(text1,text2,imageUrl)
result = data["result"]
print(result)

# MOVIE INFO
data = api.movie("avengers")
result = "Title : {}".format(data["result"]["title"])
result += "\nDuration : {}".format(data["result"]["runtime"])
result += "\nYear : {}".format(data["result"]["year"])
result += "\nRelease : {}".format(data["result"]["release"])
result += "\nDVD : {}".format(data["result"]["dvd"])
result += "\ngenre : {}".format(data["result"]["genre"])
result += "\nProduction : {}".format(data["result"]["production"])
result += "\nDirector : {}".format(data["result"]["director"])
result += "\nActors : {}".format(data["result"]["actors"])
result += "\nAwards : {}".format(data["result"]["awards"])
result += "\n\nSynopsis :\n{}".format(data["result"]["synopsis"])
result += "\n\nPoster : {}".format(data["result"]["poster"])
print(result)

# MOVIE QUOTES
data = api.movie_quotes()
result = data["result"]
print(result)

# INFO BIOSKOP
data = api.cinema("garut")
result = "Cinema 21"
result += "\n\nCity : {}\n".format(data["result"]["city"])
number = 0
for a in data["result"]["data"]:
    number += 1
    result += "\n{}. {}".format(number,a["cinema"])
print(result)

# INFO TAYANGAN BIOSKOP
data = api.cinema("garut")
number = 0
select_ = 1 # number of cinema
cinema = data["result"]["data"]
list_cinema = [o for o in cinema]
track = list_cinema[select_-1]
result = "{}".format(track["cinema"])
result += "\n{}".format(track["address"])
result += "\n\nNow playing :"
for a in track["nowPlaying"]:
    number += 1
    result += "\n{}. {}".format(number,a["movie"])
result += "\n\nStudio Image : {}".format(track["studioImage"])
print(result)

# INFO FILM BIOSKOP
data = api.cinema("garut")
number = 0
select_one = 1 # number of cinema
select_two = 1 # number of movie
showtime = ""
cinema = data["result"]["data"]
list_cinema = [o for o in cinema]
track = list_cinema[select_one-1]
list_track = [y for y in track["nowPlaying"]]
movies = list_track[select_two-1]
for x in movies["showtime"]:
    showtime += "{}, ".format(x)
result = "{}".format(movies["movie"])
result += "\n\nPrice : {}".format(movies["price"])
result += "\n\nShowtime : {}".format(showtime[:-2])
result += "\n\nGenre : {}".format(movies["genre"])
result += "\nDuration : {}".format(movies["duration"])
result += "\nDirector : {}".format(movies["director"])
result += "\nActor : {}".format(movies["actor"])
result += "\n\nSynopsis :\n{}".format(movies["synopsis"])
result += "\n\nPoster : {}".format(movies["poster"])
print(result)

# TINYURL - SHORTEDLINK
data = api.tinyurl("https://www.imjustgood.com")
result = data["result"]
print(result)

# BITLY - SHORTEDLINK
data = api.bitly("https://www.imjustgood.com")
result = data["result"]
print(result)

# CUSTOMIZE LINK
data = api.customlink("your_label", "https://example.com")
result = data["result"]
print(result)

# KBBI / KAMUS BESAR BAHASA INDONESIA
data = api.kbbi("komputer")
result = data["result"]["desc"]
print(result)

# DAILY TOP NEWS
data = api.topnews()
number = 0
result = "Top News Daily"
for a in data["result"]:
    number += 1
    result += "\n\n{}. {}".format(number,a["title"])
    result += "\nSource : {}".format(a["source"])
    result += "\nAuthor : {}".format(a["author"])
    result += "\nPage : {}".format(a["url"])
print(result)

# WIKIPEDIA
data = api.wikipedia("jakarta")
result = "Wikipedia : {}".format(query)
result += "\nDescription : {}".format(data["result"])
print(result)

# URBAN DICTIONARY
data = api.urban("dick head")
result = "Urban Dictionary"
result += "\nDefinition : {}".format(data["result"]["definition"])
result += "\nExample : {}".format(data["result"]["example"])
print(result)

# DAILY ZODIAC
data = api.zodiac("aries")
result = "\nSign : {}".format(data["result"]["zodiac"])
result += "\nCouple : {}".format(data["result"]["couple"])
result += "\nDate Range : {}".format(data["result"]["date"])
result += "\nLucky Color : {}".format(data["result"]["color"])
result += "\nLucky Time : {}".format(data["result"]["time"])
result += "\nLucky Number : {}".format(data["result"]["number"])
result += "\n\nPublic : {}".format(data["result"]["public"])
result += "\n\nMoney : {}".format(data["result"]["money"])
result += "\n\nLove Couple : {}".format(data["result"]["love"]["couple"])
result += "\n\nLove Single : {}".format(data["result"]["love"]["single"])
result += "\n\nImage : {}".format(data["result"]["image"])
print(result)

# INFO WAKTU SHOLAT
data = api.adzan("palembang")
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

# INFO CUACA / WEATHER
data = api.cuaca("surabaya")
result = "{}".format(data["result"]["location"])
result += "\nCuaca : {}".format(data["result"]["description"])
result += "\nSuhu : {}".format(data["result"]["temperature"])
result += "\nAngin : {}".format(data["result"]["wind"])
result += "\nKelembapan : {}".format(data["result"]["humidity"])
print(result)

# INFO GEMPA - BMKG
data = api.bmkg()
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

# INFO CORONA VIRUS / COVID-19
data = api.corona()
result = "CORONA VIRUS QUICKCOUNT"
result += "\n{}".format(data["result"]["date"])
result += "\n\nWorld"
result += "\nCase : {}".format(data["result"]["world"]["case"])
result += "\nFit : {}".format(data["result"]["world"]["fit"])
result += "\nRip : {}".format(data["result"]["world"]["rip"])
result += "\n\nIndonesia"
result += "\nCase : {}".format(data["result"]["indonesia"]["case"])
result += "\nFit : {}".format(data["result"]["indonesia"]["fit"])
result += "\nRip : {}".format(data["result"]["indonesia"]["rip"])
print(result)

# INFO LOWONGAN KERJA
data = api.karir()
number = 0
result = "Info Lowongan Kerja"
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

# INFO RESI PENGIRIMAN
data = api.resi("jne", "CGK2H03789568816")
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

# INFO HANDPHONE CELLULAR
data = api.cellular("iphone 12")
number = 0
result = "Spesification Cellular"
for a in data["result"]:
    result += "\n\n{}. {}".format(number,a["brands"])
    result += "\nRelease : {}".format(a["release"])
    result += "\nChipset : {}".format(a["chipset"])
    result += "\nScreen : {}".format(a["screen"])
    result += "\nBattery : {}".format(a["battery"])
    result += "\nDisplay : {}".format(a["display"])
    result += "\nRam : {}".format(a["ram"])
    result += "\nStorage : {}".format(a["storage"])
    result += "\nThumbnail : {}".format(a["thumbnail"])
    result += "\nPage : {}".format(a["pageUrl"])
print(result)

# INFO TANGGAL LAHIR
data = api.lahir("17-08-1945")
result = "Lahir : {}".format(data["result"]["lahir"])
result = "\nHari : {}".format(data["result"]["hari"])
result = "\nZodiac : {}".format(data["result"]["zodiak"])
result = "\nUltah : {}".format(data["result"]["ultah"])
result = "\nUsia : {}".format(data["result"]["usia"])
print(result)

# INFO TANGGAL JADIAN - PRIMBON
data = api.jadian("17-08-1945")
result = "Date : {}".format(data["result"]["date"])
result += "\n\nRelated : {}".format(data["result"]["related"])
result += "\n\nDescription : {}".format(data["result"]["description"])
print(result)

# ARTI NAMA - PRIMBON
data = api.nama("soekarno")
result = "Nama : {}".format(data["result"]["name"])
result += "\nKarakter : {}".format(data["result"]["definition"])
result += "\nDeskripsi : {}".format(data["result"]["description"])
print(result)

# ARTI MIMPI - PRIMBON
data = api.mimpi("ciuman")
result = "Arti Mimpi"
for a in data["result"]:
    result += "\n\nMimpi : {}".format(a["dream"])
    result += "\nArti : {}".format(a["meaning"])
print(result)

# ACARA TV SEKARANG
data = api.acaratv()
result = "Acara TV"
for a data["result"]:
    for b in a:
        result += "\n\nChannel : {}".format(b)
        for c in a[b]:
            result += "\n{}".format(c)
print(result)

# ACARA TV STASIUN
data = api.acaratv_channel("globaltv")
result = "Jadwal Acara TV"
for a in data["result"]:
    result += "\n{}".format(a)
print(result)

# CCTV CAMERA - CODE
data = api.cctv_code()
result += "DAFTAR CCTV"
for a in data["result"]["available"]:
    result += "\n{} {}".format(a,data["result"]["available"][a])
result += "\n\nCCTV AKTIF"
for b in data["result"]["active"]:
    result += "\n{} {}".format(b,data["result"]["active"][b])
print(result)

# CCTV CAMERA - INFO CODE
data = api.cctvSearch("204")
result = "CCTV CAMERA INFO"
result += "\nArea : {}".format(data["result"]["area"])
result += "\nWilayah : {}".format(data["result"]["wilayah"])
result += "\n\nThumbnail : {}".format(data["result"]["thumbnail"])
result += "\n\nVideo : {}".format(data["result"]["video"])
result += "\n\n{}".format(data["result"]["camera"])
print(result)

# MANGA - SEARCH
data = api.mangaSearch("boruto")
result = "{}".format(data["result"]["title"])
result += "\nAuthor : {}".format(data["result"]["author"])
result += "\nGenre : {}".format(data["result"]["genre"])
result += "\nRating : {}".format(data["result"]["rating"])
result += "\nRelease : {}".format(data["result"]["release"])
result += "\nStatus : {}".format(data["result"]["status"])
result += "\nType : {}".format(data["result"]["type"])
result += "\nUpdate : {}".format(data["result"]["updated"])
result += "\n\nSynopsis :\n{}".format(data["result"]["synopsis"])
result += "\n\nThumbnail : {}".format(data["result"]["thumbnail"])
print(result)

# MANGA - CHAPTER
data = api.mangaChapter("boruto-naruto-next-generations-chapter-001")
number = 0
result = "{}".format(data["result"]["title"])
for a in data["result"]["manga"]:
    number += 1
    result += "\n{}. {}".format(number,a)
print(result)

# SCREENSHOT WEB
data = api.screenshot("https://api.imjustgood.com/")
result = "Screenshot Result :"
result += "\nDekstop screen : {}".format(data["result"]["desktop"])
result += "\nMobile screen : {}".format(data["result"]["mobile"])
print(result)

# GIF SEARCH
data = api.gif("coding")
result = random.choice(data["result"])
print(result)

# IMAGE TO URL - CONVERT
data = api.imgurl("Image/example.jpg")
result = data["result"]
print(result)

# TEXT TO IMAGE
data = api.imagetext("Welcome to Imjustgood.com")
result = data["result"]
print(result)

# WATERMARK - TEXT
data = api.watermark_text("https://example.com/image.jpg", "IMJUSTGOOD")
result = data["result"]
print(result)

# WATERMARK - IMAGE PNG
data = api.watermark_text("https://example.com/image.jpg", "https://example.com/icon.png")
result = data["result"]
print(result)

# SIMISIMI
data = api.simisimi("kenapa anda jomnlo ?")
result = data["result"]
print(result)

# CALCULATOR
data = api.calc("10+10x10:10-10")
result = data["result"]
print(result)

# CHECK IP
data = api.check_ip("8.8.8.8")
result = "Ip Address : {}".format(data["result"]["ip_address"])
for a in data["result"]:
    if a != "ip_address" and a != "languages" and data["result"][a] is not None:
       result += "\n{} : {}".format(a.title(),data["result"][a])
languages = "\nLanguage : "
for b in data["result"]["languages"]:
    languages += "{}, ".format(b)
result += languages[:-2]
print(result)

# BINARY ENCODE
data = api.BinaryEncode("Imjustgood")
result = data["result"]
print(result)

# BINARY DECODE
data = api.BinaryDecode("01001001011011010110101001110101011100110111010001100111011011110110111101100100")
result = data["result"]
print(result)

# BASE64 ENCODE
data = api.B64Encode("Imjustgood")
result = data["result"]
print(result)

# BASE64 DECODE
data = api.B64Decode("VGhlQXV0b2JvdHNDb3Jw")
result = data["result"]
print(result)

# ASCII TEXT
data = api.ascii("imjustgood")
print(data)

# FANCY TEXT
data = api.fancy("IMJUSTGOOD")
result = ""
for s in data["result"]:
    result += "\n{}\n".format(s)
print(result)

''' INFORMATION UPDATE AVALAIBLE ON :
WEBSITE  - https://api.imjustgood.com/apidoc
TIMELINE - https://api.imjustgood.com/custom/announcements '''
