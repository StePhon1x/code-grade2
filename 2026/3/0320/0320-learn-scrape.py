# scrape-豆瓣/top250

import requests
from bs4 import BeautifulSoup
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0",
}

for start_num in range(0, 250, 25):
    response = requests.get(f"https://movie.douban.com/top250?start={start_num}", headers=headers)

    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    soup_titles = soup.findAll("div", attrs={"class": "hd"})

    for idx, title in enumerate(soup_titles, start=start_num+1):
        title_cn = title.find("span")
        print(f"TOP{idx}: {title_cn.string}")
    time.sleep(1.5)