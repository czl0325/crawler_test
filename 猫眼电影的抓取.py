import requests
from 

base_url = "https://maoyan.com"
movies = []
for page in range(3):
    response = requests.get("{}/films?showType=3&offset={}".format(base_url, page*30))
    covers =