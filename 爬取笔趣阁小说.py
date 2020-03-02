from selenium import webdriver
import requests
import re
import os
import time

class FictionSpider:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}
        self.start_url = "http://m.xbiquge.la/wapbook/52679_22317001.html"
        if os.path.exists("烽火三国志.txt"):
            os.remove("烽火三国志.txt")

    def run(self):
        while True:
            print("请求网址：", self.start_url)
            res = requests.get(self.start_url, headers=self.headers)
            res = res.content.decode()
            content = re.findall('<div id="nr1">(.*?)</div>', res, re.S)
            if len(content) > 0:
                content = content[0]
                content = re.sub("<br.*>+", "\n", content)
                content = re.sub("\n+", "\n", content)
                content = re.sub("&nbsp;", " ", content)
                self.save_content(content)
                print("保存成功!")
            else:
                print("未找到数据:\n", res)
                break
            next_url = re.findall('<a id="pt_next" href="(.*?)">', res)
            if len(next_url) == 0:
                print("未找到下一页的链接:\n",res)
                break
            next_url = "http://m.xbiquge.la" + next_url[0]
            self.start_url = next_url
            time.sleep(3)


    def save_content(self, content):
        with open("烽火三国志.txt", "a") as f:
            f.write(content)
            f.write("\n")


if __name__ == '__main__':
    fictionSpider = FictionSpider()
    fictionSpider.run()
