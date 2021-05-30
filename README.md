## API.IMJUSTGOOD.COM
```
█ █▀▄▀█   █ █ █ █▀ ▀█▀ █▀▀ █▀█ █▀█ █▀▄
█ █ ▀ █ █▄█ █▄█ ▄█  █  █▄█ █▄█ █▄█ █▄▀
api media service to make your code more better.
```
<p>
    <a href="http://pypi.org/project/justgood" rel="nofollow">
        <img alt="PyPI" src="https://img.shields.io/pypi/v/justgood?label=PyPI" style="max-width:100%;">
    </a>
    <a href="https://github.com/RendyTR/api.imjustgood.com" rel="nofollow">
        <img alt="Update" src="https://img.shields.io/github/last-commit/rendytr/api.imjustgood.com?color=red&label=Update" height="20" style="max-width:100%;">
    </a>
    <a href="https://github.com/RendyTR" rel="nofollow">
        <img alt="Views" src="https://komarev.com/ghpvc/?username=RendyTR&color=green&label=Views" height="20" style="max-width:100%;">
    </a>
</p>

### Documentation
Full documentation available on https://api.imjustgood.com

### Installation
```
pip install justgood
```

### Upgrade
```
pip install --upgrade justgood
```

### Example
Here is how to use the module in your own python code. we choose <a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/instapost.py">instapost</a> media as an example.
```python
from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
url = "https://instagram.com/p/COjHqwGhFA6/"
data = media.instapost(url)

print(data)
```

Response results
```json
{
    "creator": "ImJustGood", 
    "result": {
        "caption": "GET STARTED NOW\nhttps://api.imjustgood.com\n#autobots #rendytr #imjustgood", 
        "created": "2 weeks ago", 
        "fullname": "The Autobots Corporation", 
        "likes": "8",
        "picture": "https://scontent-iad3-2.cdninstagram.com/v/t51.2885-19/s150x150/156716508_792361228290684_2737571466878743960_n.jpg?tp=1&_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_ohc=rpY8_az5H7gAX-ixW8W&edm=AP_V10EBAAAA&ccb=7-4&oh=660db30b81c81cf4eb6904c4937aa066&oe=60B73467&_nc_sid=4f375e", 
        "postData": [
            {
                "postUrl": "https://scontent-iad3-2.cdninstagram.com/v/t51.2885-15/e35/p1080x1080/182551939_1505660729785431_4872170436067358847_n.jpg?tp=1&_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_cat=103&_nc_ohc=4hwRibBJhRsAX-elcAw&edm=AP_V10EBAAAA&ccb=7-4&oh=d64890598377516a254a6d8bf5bdad41&oe=60B680F5&_nc_sid=4f375e", 
                "type": "image"
            }, 
            {
                "postUrl": "https://scontent-iad3-2.cdninstagram.com/v/t51.2885-15/e35/p1080x1080/182772702_212190447098888_3451476763231220039_n.jpg?tp=1&_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_cat=108&_nc_ohc=nacAdgapPioAX9oO99M&edm=AP_V10EBAAAA&ccb=7-4&oh=b605fbc309664405b8d1d936fe9b30ce&oe=60B6E2F7&_nc_sid=4f375e", 
                "type": "image"
            }, 
            {
                "postUrl": "https://scontent-iad3-2.cdninstagram.com/v/t50.2886-16/183065958_515613456128123_180962327655226030_n.mp4?_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_cat=111&_nc_ohc=HqRjnESsF-cAX8o4AeL&edm=AP_V10EBAAAA&ccb=7-4&oe=60B25D7F&oh=ce2f464d4ef43106620b6bf68f443b99&_nc_sid=4f375e", 
                "poster": "https://scontent-iad3-2.cdninstagram.com/v/t51.2885-15/e35/182468569_529144071448455_8659487135953051116_n.jpg?tp=1&_nc_ht=scontent-iad3-2.cdninstagram.com&_nc_cat=103&_nc_ohc=UT35RAAdxOIAX8MGqk9&edm=AP_V10EBAAAA&ccb=7-4&oh=9370c6ee9c9a32123800ddb5492aa37d&oe=60B2A563&_nc_sid=4f375e", 
                "type": "video"
            }
        ], 
        "slidePost": true, 
        "username": "the.autobots_corp"
    }, 
    "status": 200
}
```

Get certain attributes
```
>>> username = data["result"]["username"]
>>> print(username)
the.autobots_corp

>>> fullname = data["result"]["fullname"]
>>> print(fullname)
The Autobots Corporation

>>> created = data["result"]["created"]
>>> print(created)
2 days ago

>>> caption = data["result"]["caption"]
>>> print(caption)
GET STARTED NOW
https://api.imjustgood.com
#autobots #rendytr #imjustgood

>>> picture = data["result"]["picture"]
>>> print(picture)
https://scontent-sin6-1.cdninstagram.com/v/t51.2885-19/s150x150/135785550_234471278085178_3734782670290828910_n.jpg?_nc_ht=scontent-sin6-1.cdninstagram.com&_nc_ohc=HQdOrvJcYNYAX-g_hAo&tp=1&oh=4780e9fa82b62dd71356498dfed7c362&oe=6022085E

>>> for a in data["result"]["postData"]:
...     print(a["postUrl"])
https://scontent-sin6-1.cdninstagram.com/v/t51.2885-15/sh0.08/e35/p640x640/135665982_715565716018895_1563117747618145065_n.jpg?_nc_ht=scontent-sin6-1.cdninstagram.com&_nc_cat=111&_nc_ohc=A0n5IQVkjiAAX8VxJAr&tp=1&oh=427134cb92b3ce8ed9179dab92482ad2&oe=60232E2A
https://scontent-sin6-2.cdninstagram.com/v/t50.2886-16/136676648_446366420077083_6874742578521195210_n.mp4?_nc_ht=scontent-sin6-2.cdninstagram.com&_nc_cat=103&_nc_ohc=mEzo-awDsoYAX9wKFgP&oe=5FFBC9C2&oh=725ceccf6e4668be7b8a4be70afbd7aa
```

### More Media Fitures
<table>
    <tbody>
        <tr>
            <td>Apikey Status</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/apikey_status.py">Example</a></td>
        </tr>
        <tr>
            <td>Youtube Search</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/youtube.py">Example</a></td>
        </tr>
        <tr>
            <td>Youtube Downloader</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/youtubedl.py">Example</a></td>
        </tr>
        <tr>
            <td>Joox Music</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/joox.py">Example</a></td>
        </tr>
        <tr>
            <td>Lyric Finder</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/lyric.py">Example</a></td>
        </tr>
        <tr>
            <td>Smule Profile</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/smule.py">Example</a></td>
        </tr>
        <tr>
            <td>Smule Downloader</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/smuledl.py">Example</a></td>
        </tr>
        <tr>
            <td>TikTok Profile</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/tiktok.py">Example</a></td>
        </tr>
        <tr>
            <td>TikTok Downloader</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/tiktokdl.py">Example</a></td>
        </tr>
        <tr>
            <td>Instagram Profile</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/instagram.py">Example</a></td>
        </tr>
        <tr>
            <td>Instagram Post</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/instapost.py">Example</a></td>
        </tr>
        <tr>
            <td>Instagram Story</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/instastory.py">Example</a></td>
        </tr>
        <tr>
            <td>Twitter Profile</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/twitter.py">Example</a></td>
        </tr>
        <tr>
            <td>Twitter Downloader</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/twitterdl.py">Example</a></td>
        </tr>
        <tr>
            <td>Facebook Downloader</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/facebookdl.py">Example</a></td>
        </tr>
        <tr>
            <td>GitHub Profile</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/github.py">Example</a></td>
        </tr>
        <tr>
            <td>LINE Secondary</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/line_secondary.py">Example</a></td>
        </tr>
        <tr>
            <td>LINE Timeline</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/line_timeline.py">Example</a></td>
        </tr>
        <tr>
            <td>LINE App Version</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/line_version.py">Example</a></td>
        </tr>
        <tr>
            <td>Google Search</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/google_search.py">Example</a></td>
        </tr>
        <tr>
            <td>Google Image</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/images.py">Example</a></td>
        </tr>
        <tr>
            <td>Google Playstore</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/playstore.py">Example</a></td>
        </tr>
        <tr>
            <td>Google Translate</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/translate.py">Example</a></td>
        </tr>
        <tr>
            <td>Wallpaper HD</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/wallpaper.py">Example</a></td>
        </tr>
        <tr>
            <td>Porn Videos</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/porn.py">Example</a></td>
        </tr>
        <tr>
            <td>Pornstar</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/pornstar.py">Example</a></td>
        </tr>
        <tr>
            <td>Hentai</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/hentai.py">Example</a></td>
        </tr>
        <tr>
            <td>Kamasutra</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/kamasutra.py">Example</a></td>
        </tr>
        <tr>
            <td>Dick Analyze</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/dick.py">Example</a></td>
        </tr>
        <tr>
            <td>Tits Analyze</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/tits.py">Example</a></td>
        </tr>
        <tr>
            <td>Vagina Analyze</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/vagina.py">Example</a></td>
        </tr>
        <tr>
            <td>Meme Generator</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/meme.py">Example</a></td>
        </tr>
        <tr>
            <td>Movie Review</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/movie.py">Example</a></td>
        </tr>
        <tr>
            <td>Movie Quotes</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/movie_quotes.py">Example</a></td>
        </tr>
        <tr>
            <td>Cinema 21</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/cinema.py">Example</a></td>
        </tr>
        <tr>
            <td>TinyUrl</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/tinyurl.py">Example</a></td>
        </tr>
        <tr>
            <td>Bit.ly</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/bitly.py">Example</a></td>
        </tr>
        <tr>
            <td>KBBI</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/kbbi.py">Example</a></td>
        </tr>
        <tr>
            <td>Top News</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/topnews.py">Example</a></td>
        </tr>
        <tr>
            <td>Wikipedia</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/wikipedia.py">Example</a></td>
        </tr>
        <tr>
            <td>Urban Dictionary</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/urban.py">Example</a></td>
        </tr>
        <tr>
            <td>Zodiac Daily</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/zodiac.py">Example</a></td>
        </tr>
        <tr>
            <td>Info Waktu Sholat</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/adzan.py">Example</a></td>
        </tr>
        <tr>
            <td>Info Cuaca Dunia</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/cuaca.py">Example</a></td>
        </tr>
        <tr>
            <td>Info Gempa BMKG</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/bmkg.py">Example</a></td>
        </tr>
        <tr>
            <td>Info Corona Virus</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/corona.py">Example</a></td>
        </tr>
        <tr>
            <td>Info Lowongan Kerja</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/karir.py">Example</a></td>
        </tr>
        <tr>
            <td>Info Resi Pengiriman</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/resi.py">Example</a></td>
        </tr>
        <tr>
            <td>Info Phone Cellular</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/cellular.py">Example</a></td>
        </tr>
        <tr>
            <td>Info Tanggal Lahir</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/lahir.py">Example</a></td>
        </tr>
        <tr>
            <td>Info Tanggal Jadian</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/jadian.py">Example</a></td>
        </tr>
        <tr>
            <td>Arti Nama</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/nama.py">Example</a></td>
        </tr>
        <tr>
            <td>Arti Mimpi</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/mimpi.py">Example</a></td>
        </tr>
        <tr>
            <td>Acara TV Saat Ini</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/acaratv.py">Example</a></td>
        </tr>
        <tr>
            <td>Acara TV Stasiun</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/acaratv_channel.py">Example</a></td>
        </tr>
        <tr>
            <td>CCTV Camera Code</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/cctv_code.py">Example</a></td>
        </tr>
        <tr>
            <td>CCTV Camera Search</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/cctv_search.py">Example</a></td>
        </tr>
        <tr>
            <td>Manga Search</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/manga_search.py">Example</a></td>
        </tr>
        <tr>
            <td>Manga Chapter</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/manga_chapter.py">Example</a></td>
        </tr>
        <tr>
            <td>Calculator</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/calc.py">Example</a></td>
        </tr>
        <tr>
            <td>Languages Code</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/langcode.py">Example</a></td>
        </tr>
        <tr>
            <td>Check IP Address</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/check_ip.py">Example</a></td>
        </tr>
        <tr>
            <td>Binary Encode</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/binary_encode.py">Example</a></td>
        </tr>
        <tr>
            <td>Binary Decode</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/binary_decode.py">Example</a></td>
        </tr>
        <tr>
            <td>Base64 Encode</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/b64encode.py">Example</a></td>
        </tr>
        <tr>
            <td>Base64 Decode</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/b64decode.py">Example</a></td>
        </tr>
        <tr>
            <td>Screenshot Web</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/screenshot.py">Example</a></td>
        </tr>
        <tr>
            <td>ASCII Text</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/ascii.py">Example</a></td>
        </tr>
        <tr>
            <td>Fancy Text</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/fancy.py">Example</a></td>
        </tr>
        <tr>
            <td>Customize URL</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/customlink.py">Example</a></td>
        </tr>
        <tr>
            <td>GIF Search</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/gif.py">Example</a></td>
        </tr>
        <tr>
            <td>Convert Image to URL</td>
            <td><a href="https://github.com/RendyTR/api.imjustgood.com/blob/main/Example/convert-image.py">Example</a></td>
        </tr>
    </tbody>
</table>

### Contact us here
* <a href="https://imjustgood.com/team">Imjustgood Team</a>
* <a href="https://bit.ly/2K5Lbx4">LINE Openchat Room</a>
