import re
import requests
import json

# 36kr通过最早一条数据的b_id去请求后面10条的数据

headers = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1"}

b_id = ""
while True:
    url = "https://36kr.com/pp/api/aggregation-entity?type=web_latest_article&b_id={}&per_page=10".format(b_id)
    response = requests.get(url, headers=headers)
    res = response.content.decode()
    res = json.loads(res, encoding="utf-8")
    if len(res) <= 0:
        break
    for index, item in enumerate(res["data"]["items"]):
        print("抓取到的id=%s,标题=%s" % (item["id"], item["post"]["title"]))
        if index == len(res["data"]["items"])-1:
            b_id = item["id"]