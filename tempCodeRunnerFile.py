from flask import Flask , render_template
from bs4 import BeautifulSoup
import requests
url = "https://www.businesstoday.in/jobs"
req = requests.get(url)
soup = BeautifulSoup(req.content , "html.parser")
outer_data = soup.find_all("div" , class_ = "content-area" , limit=6)