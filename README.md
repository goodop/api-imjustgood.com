## API.IMJUSTGOOD.COM
API Media service to make your code more better.
<p>
<img alt="PyPI" src="https://img.shields.io/pypi/v/justgood" style="max-width:100%;">
<img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/JUSTGOOD?color=orange" style="max-width:100%;">
<img alt="Status" src="https://img.shields.io/static/v1?label=status&message=online&color=green style="max-width:100%;">
<img alt="GitHub" src="https://img.shields.io/github/license/goodop/api-imjustgood.com" style="max-width:100%;">
</p>


### Documentation
Full documentation available on https://api.imjustgood.com

### Installation
```python
pip install justgood
```

### Example
Here is how to use the module in your own python code. we choose <a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/instapost.py">instapost</a> media as an example.
```python
from justgood import imjustgood

media = imjustgood("YOUR_APIKEY_HERE")
post_url = "https://instagram.com/p/CJtqfEbhpjO/"
data = media.instapost(post_url)

print(data)
```

Response results
```json
{
    "creator": "ImJustGood", 
    "result": {
        "caption": "Get Started\napi.imjustgood.com\n.\n#imjustgood #tac #theautobotscorp", 
        "created": "2 days ago", 
        "fullname": "The Autobots Corporation", 
        "picture": "https://scontent-sin6-1.cdninstagram.com/v/t51.2885-19/s150x150/135785550_234471278085178_3734782670290828910_n.jpg?_nc_ht=scontent-sin6-1.cdninstagram.com&_nc_ohc=HQdOrvJcYNYAX-g_hAo&tp=1&oh=4780e9fa82b62dd71356498dfed7c362&oe=6022085E", 
        "postData": [
            {
                "postUrl": "https://scontent-sin6-1.cdninstagram.com/v/t51.2885-15/sh0.08/e35/p640x640/135665982_715565716018895_1563117747618145065_n.jpg?_nc_ht=scontent-sin6-1.cdninstagram.com&_nc_cat=111&_nc_ohc=A0n5IQVkjiAAX8VxJAr&tp=1&oh=427134cb92b3ce8ed9179dab92482ad2&oe=60232E2A", 
                "type": "image"
            },
            {
                "postUrl": "https://scontent-sin6-2.cdninstagram.com/v/t50.2886-16/136676648_446366420077083_6874742578521195210_n.mp4?_nc_ht=scontent-sin6-2.cdninstagram.com&_nc_cat=103&_nc_ohc=mEzo-awDsoYAX9wKFgP&oe=5FFBC9C2&oh=725ceccf6e4668be7b8a4be70afbd7aa", 
                "poster": "https://scontent-sin6-3.cdninstagram.com/v/t51.2885-15/e35/135519816_2504157059888884_6711864394916943089_n.jpg?_nc_ht=scontent-sin6-3.cdninstagram.com&_nc_cat=104&_nc_ohc=yy5oCKYuc-sAX9JgZjA&tp=1&oh=d0d48a6eb5275bf296eb8e05128a3882&oe=5FFB7530", 
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
Get Started
api.imjustgood.com
.
#imjustgood #tac #theautobotscorp

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
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/apikey_status.py">Example</a></td>
        </tr>
        <tr>
            <td>Youtube Search</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/youtube.py">Example</a></td>
        </tr>
        <tr>
            <td>Youtube Downloader</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/youtubedl.py">Example</a></td>
        </tr>
        <tr>
            <td>Joox Music</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/joox.py">Example</a></td>
        </tr>
        <tr>
            <td>Lyric Finder</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/lyric.py">Example</a></td>
        </tr>
        <tr>
            <td>Smule Profile</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/smule.py">Example</a></td>
        </tr>
        <tr>
            <td>Smule Downloader</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/smuledl.py">Example</a></td>
        </tr>
        <tr>
            <td>TikTok Profile</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/tiktok.py">Example</a></td>
        </tr>
        <tr>
            <td>TikTok Downloader</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/tiktokdl.py">Example</a></td>
        </tr>
        <tr>
            <td>Instagram Profile</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/instagram.py">Example</a></td>
        </tr>
        <tr>
            <td>Instagram Post</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/instapost.py">Example</a></td>
        </tr>
        <tr>
            <td>Instagram Story</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/instastory.py">Example</a></td>
        </tr>
        <tr>
            <td>Twitter Profile</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/twitter.py">Example</a></td>
        </tr>
        <tr>
            <td>GitHub Profile</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/github.py">Example</a></td>
        </tr>
        <tr>
            <td>Google Playstore</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/playstore.py">Example</a></td>
        </tr>
        <tr>
            <td>Google Translate</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/translate.py">Example</a></td>
        </tr>
        <tr>
            <td>Google Image</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/images.py">Example</a></td>
        </tr>
        <tr>
            <td>Wallpaper HD</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/wallpaper.py">Example</a></td>
        </tr>
        <tr>
            <td>Porn Videos</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/porn.py">Example</a></td>
        </tr>
        <tr>
            <td>Pornstar</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/pornstar.py">Example</a></td>
        </tr>
        <tr>
            <td>Hentai</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/hentai.py">Example</a></td>
        </tr>
        <tr>
            <td>Kamasutra</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/kamasutra.py">Example</a></td>
        </tr>
        <tr>
            <td>Dick Analyze</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/dick.py">Example</a></td>
        </tr>
        <tr>
            <td>Tits Analyze</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/tits.py">Example</a></td>
        </tr>
        <tr>
            <td>Vagina Analyze</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/vagina.py">Example</a></td>
        </tr>
        <tr>
            <td>Meme Generator</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/meme.py">Example</a></td>
        </tr>
        <tr>
            <td>Movie Review</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/movie.py">Example</a></td>
        </tr>
        <tr>
            <td>Movie Quotes</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/movie_quotes.py">Example</a></td>
        </tr>
        <tr>
            <td>Cinema 21</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/cinema.py">Example</a></td>
        </tr>
        <tr>
            <td>TinyUrl</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/tinyurl.py">Example</a></td>
        </tr>
        <tr>
            <td>Bit.ly</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/bitly.py">Example</a></td>
        </tr>
        <tr>
            <td>Top News</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/topnews.py">Example</a></td>
        </tr>
        <tr>
            <td>Wikipedia</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/wikipedia.py">Example</a></td>
        </tr>
        <tr>
            <td>Urban Dictionary</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/urban.py">Example</a></td>
        </tr>
        <tr>
            <td>Zodiac Daily</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/zodiac.py">Example</a></td>
        </tr>
        <tr>
            <td>Info Waktu Sholat</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/adzan.py">Example</a></td>
        </tr>
        <tr>
            <td>Info Cuaca Dunia</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/cuaca.py">Example</a></td>
        </tr>
        <tr>
            <td>Info Gempa BMKG</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/bmkg.py">Example</a></td>
        </tr>
        <tr>
            <td>Info Corona Virus</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/corona.py">Example</a></td>
        </tr>
        <tr>
            <td>Info Lowongan Kerja</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/karir.py">Example</a></td>
        </tr>
        <tr>
            <td>Info Resi Pengiriman</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/resi.py">Example</a></td>
        </tr>
        <tr>
            <td>Info Phone Cellular</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/cellular.py">Example</a></td>
        </tr>
        <tr>
            <td>Info Tanggal Lahir</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/lahir.py">Example</a></td>
        </tr>
        <tr>
            <td>Info Tanggal Jadian</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/jadian.py">Example</a></td>
        </tr>
        <tr>
            <td>Arti Nama</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/nama.py">Example</a></td>
        </tr>
        <tr>
            <td>Arti Mimpi</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/mimpi.py">Example</a></td>
        </tr>
        <tr>
            <td>Acara TV Saat Ini</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/acaratv.py">Example</a></td>
        </tr>
        <tr>
            <td>Acara TV Stasiun</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/acaratv_channel.py">Example</a></td>
        </tr>
        <tr>
            <td>CCTV Camera Code</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/cctv_code.py">Example</a></td>
        </tr>
        <tr>
            <td>CCTV Camera Search</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/cctv_search.py">Example</a></td>
        </tr>
        <tr>
            <td>Manga Search</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/manga_search.py">Example</a></td>
        </tr>
        <tr>
            <td>Manga Chapter</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/manga_chapter.py">Example</a></td>
        </tr>
        <tr>
            <td>Calculator</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/calc.py">Example</a></td>
        </tr>
        <tr>
            <td>Languages Code</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/langcode.py">Example</a></td>
        </tr>
        <tr>
            <td>Check IP Address</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/check_ip.py">Example</a></td>
        </tr>
        <tr>
            <td>Binary Encode</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/binary_encode.py">Example</a></td>
        </tr>
        <tr>
            <td>Binary Decode</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/binary_decode.py">Example</a></td>
        </tr>
        <tr>
            <td>Base64 Encode</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/b64encode.py">Example</a></td>
        </tr>
        <tr>
            <td>Base64 Decode</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/b64decode.py">Example</a></td>
        </tr>
        <tr>
            <td>LINE Timeline</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/line_timeline.py">Example</a></td>
        </tr>
        <tr>
            <td>LINE App Version</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/line_version.py">Example</a></td>
        </tr>
        <tr>
            <td>Screenshot Web</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/screenshot.py">Example</a></td>
        </tr>
        <tr>
            <td>ASCII Text</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/ascii.py">Example</a></td>
        </tr>
        <tr>
            <td>Custom URL</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/customlink.py">Example</a></td>
        </tr>
        <tr>
            <td>Convert Image to URL</td>
            <td><a href="https://github.com/goodop/api-imjustgood.com/blob/main/Example/convert-image.py">Example</a></td>
        </tr>
    </tbody>
</table>

### Contact us
* <a href="https://imjustgood.com/team">Imjustgood Team</a>
* <a href="https://bit.ly/2K5Lbx4">LINE Openchat Room</a>
