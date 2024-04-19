# 初めてのスクレイピング
import requests
from bs4 import BeautifulSoup


url = "https://www.yahoo.co.jp/"
response = requests.get(url)
html = response.text

data =  BeautifulSoup(html , "html.parser")

print(data)