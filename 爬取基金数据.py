import requests
import time
import json
import xlrd
import xlwt
import datetime
import os
from openpyxl import load_workbook
from openpyxl import Workbook


class FundSpider:
    def __init__(self):
        self.url_temp = "https://fundmobapi.eastmoney.com/FundMNewApi/FundMNNetNewList?fundtype=0&SortColumn=RZDF&Sort=desc&pageIndex={}&pagesize=30&deviceid=Wap&plat=Wap&product=EFund&version=2.0.0&_={}"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}

    def save_content(self, content):
        pass

    def run(self):
        page_index = 1

        wb = Workbook()
        ws = wb.active
        while True:
            url = self.url_temp.format(page_index, int(round(time.time() * 1000)))
            print(url)
            response = requests.get(url, headers=self.headers).content.decode()
            response = json.loads(response, encoding="utf-8")
            if len(response["Datas"]) > 0:
                res = response["Datas"][0]
                if len(res) > 0:
                    for i, fund in enumerate(res):
                        if i == 0 and page_index == 1:
                            ws.append([fund["FSRQ"]])
                        ws.append([fund["FCODE"] + "|" + fund["SHORTNAME"] + "|" + fund["DWJZ"] + "|" + fund["RZDF"]])
                    page_index += 1
                    if page_index > 30:
                        break
                    time.sleep(3)
                else:
                    print("抓取结束")
                    break
            else:
                print("抓取结束")
                break
        wb.save('基金.xlsx')


if __name__ == '__main__':
    # print((datetime.datetime.now()+datetime.timedelta(days=-1)).strftime("%Y-%m-%d"))
    fund_spider = FundSpider()
    fund_spider.run()

    # str = "a   !@# b"
    # print(re.search("a[^\w]*", str).group())
