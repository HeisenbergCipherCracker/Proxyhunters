import requests
from bs4 import BeautifulSoup

response = requests.get("https://proxyscrape.com/free-proxy-list")
print(response.text)