import requests
from lxml import etree

base_url = "https://seatory.tuchong.com/6965607/"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"
}
response = requests.get(base_url, headers=headers)
response.encoding = response.apparent_encoding
e = etree.HTML(response.text)
img_urls = e.xpath('//img[@class="multi-photo-image"]/@src')
for url in img_urls:
    res = requests.get(url, headers=headers)
    img_name = url[url.rfind("/")+1:]
    with open("image/"+img_name, "wb") as f:
        f.write(res.content)
