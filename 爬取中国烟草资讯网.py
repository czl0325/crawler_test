import requests
import re

headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"
}

url = "http://www.echinatobacco.com/html/site27/yyfwz/index.html"
html_str = requests.get(url, headers=headers)
html_str = html_str.content.decode()
res = re.findall(r'<em><a href="(.*?)">(.*?)</a></em><span>(.*?)</span>', html_str)
for new in res:
    print("抓取到网址：{}，标题：{}，时间：{}".format(new[0],new[1],new[2]))