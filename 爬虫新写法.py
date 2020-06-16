import requests
from lxml import etree

base_url = "https://www.qiushibaike.com"
# url管理
class URLManage(object):
    def __init__(self):
        self.old_urls = []
        self.new_urls = []

    # 取一个url
    def get_new_url(self):
        url = self.new_urls.pop()
        self.old_urls.append(url)
        return url

    def add_new_url(self, url):
        if url not in self.old_urls and url not in self.new_urls and url is not None:
            self.new_urls.append(url)

    def add_new_urls(self, urls):
        for url in urls:
            self.add_new_url(url)

    # 是否还有可爬取的url
    def has_new_url(self):
        return self.get_new_url_size() > 0

    # 可爬取的数量
    def get_new_url_size(self):
        return len(self.new_urls)

    # 已经爬取的数量
    def get_old_url_size(self):
        return len(self.old_urls)


# 爬取管理器
class Downloader(object):
    def download(self, url):
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.content.decode("utf8")
        else:
            return None


# 解析管理类
class Parser(object):
    def parse(self, html):
        e = etree.HTML(html)
        authors = e.xpath('//div[@class="col1 old-style-col1"]//div[ contains(@class, "article block")]//a//h2')
        contents = e.xpath('//div[@class="col1 old-style-col1"]//div[ contains(@class, "article block")]//div[@class="content"]/span[1]')
        datas = []
        for author, content in zip(authors, contents):
            str = "作者：%s \n内容：%s" % (author.xpath('normalize-space(./text())'), content.xpath('normalize-space(./text())'))
            print(str)
            datas.append(str)
        urls = e.xpath('//ul[@class="pagination"]/li/a/@href')
        urls = [base_url + url for url in urls]
        return datas, urls




# 数据处理类
class DataOperator(object):
    def save(self, data):
        pass


# 调度
class Dispatch(object):
    def __init__(self):
        self.downloader = Downloader()
        self.url_manager = URLManage()
        self.parser = Parser()
        self.data_operator = DataOperator()

    def run(self, url):
        self.url_manager.add_new_url(url)
        while self.url_manager.has_new_url():
            my_url = self.url_manager.get_new_url()
            html = self.downloader.download(my_url)
            if html is not None:
                data, urls = self.parser.parse(html)
                self.data_operator.save(data)
                self.url_manager.add_new_urls(urls)


if __name__ == '__main__':
    dispatch = Dispatch()
    dispatch.run("https://www.qiushibaike.com/text/page/1")