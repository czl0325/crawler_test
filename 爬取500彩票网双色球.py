import requests
from lxml import etree

base_url = "https://datachart.500.com/ssq/"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"
}
response = requests.get(base_url, headers=headers)
e = etree.HTML(response.content)
trs = e.xpath('//tbody[@id="tdata"]/tr[not(@class)]')
for tr in trs:
    periods = tr.xpath('normalize-space(./td[1]/text())')
    red_bolls = tr.xpath('./td[@class="chartBall01"]/text()')
    blue_bolls = tr.xpath('./td[@class="chartBall02"]/text()')
    print("第%s期，红球：%s，篮球：%s" % (periods, ",".join(red_bolls), blue_bolls[0]))