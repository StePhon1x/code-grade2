import requests
from bs4 import BeautifulSoup
import pyodbc 
import time

# --- 连接 SSMS 中的 SQL Server ---
# Driver: 驱动程序，通常 Windows 自带 'SQL Server'
# Server: 你的服务器名称（SSMS 登录时看到的那个）
# Database: 刚才创建的数据库名
conn_str = (
    'DRIVER={SQL Server};'
    'SERVER=.\SQLEXPRESS;'  # 这里填你的服务器名，点表示本机
    'DATABASE=DoubanDB;'
    'Trusted_Connection=yes;' # 使用 Windows 身份验证
)
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0",
}

for start_num in range(0, 250, 25):
    response = requests.get(f"https://movie.douban.com/top250?start={start_num}", headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    items = soup.find_all("div", class_="item")

    for item in items:
        rank = item.find("em").text
        title = item.find("span", class_="title").text
        rating = item.find("span", class_="rating_num").text

        # 插入 SQL Server
        cursor.execute("INSERT INTO Movies (Rank, Title, Rating) VALUES (?, ?, ?)", 
                    (rank, title, rating))
    
    conn.commit()
    print(f"第 {start_num+1} 页已同步到你的数据库")
    time.sleep(1.5)

conn.close()