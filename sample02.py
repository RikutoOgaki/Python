# 初めてのスクレイピング
import requests
url = "https://example.com"
response = requests.get(url)
html = response.text