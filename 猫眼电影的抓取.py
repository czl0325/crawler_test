import requests
from lxml import etree
import urllib3
from urllib3.exceptions import InsecureRequestWarning
from selenium import webdriver
import time

urllib3.disable_warnings(InsecureRequestWarning)

maoyan_url = "https://maoyan.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36"
}
movies = []


# driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver")
# driver.get(maoyan_url)
# time.sleep(3)
# e = etree.HTML(driver.page_source)
# names = e.xpath("//span[@class='name noscore']/text")
# print(names)

# # for page in range(1):
response = requests.get(maoyan_url, headers=headers)
response.encoding = response.apparent_encoding

e = etree.HTML(response.text)
names = e.xpath('//div[@class="panel"][2]//div[@class="movie-title"]/text()')
dates = e.xpath('//div[@class="panel"][2]//div[@class="movie-detail movie-rt"]/text()')
for name, date in zip(names, dates):
    print(date, name)