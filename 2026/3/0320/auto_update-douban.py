# 20260323 加入弹窗功能 可弹出每日推荐电影

import requests  # 发送 HTTP 请求，用来下载网页内容
from bs4 import BeautifulSoup  # 解析 HTML，从网页中提取数据（"网页解剖刀"）
import pyodbc  # 连接 Windows 上的 SQL Server 数据库
import time  # 提供 time.sleep()，爬取间隔防止被封 IP
import customtkinter as ctk  # 现代风格的 tkinter UI 库，用来做弹窗
import webbrowser  # 调用系统默认浏览器打开链接


def auto_update_and_recommend():
    # 1. 连接 SSMS
    conn_str = "DRIVER={SQL Server};SERVER=.\SQLEXPRESS;DATABASE=DoubanDB;Trusted_Connection=yes;"
    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
    except Exception as e:
        print(f"数据库连接失败: {e}")
        return

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 Edg/145.0.0.0",
    }

    print("开始自动更新豆瓣 Top 250...")

    # 2. 爬取并同步到数据库
    for start_num in range(0, 250, 25):
        try:
            url = f"https://movie.douban.com/top250?start={start_num}"
            url = f"https://movie.douban.com/top250?start={start_num}"
            res = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(res.text, "html.parser")
            items = soup.find_all("div", class_="item")

            for item in items:
                rank = item.find("em").text
                title = item.find("span", class_="title").text
                rating = item.find("span", class_="rating_num").text
                movie_url = item.find("a")["href"]

                # 3. 调用存储过程
                cursor.execute(
                    "{CALL sp_UpdateMovieRank (?, ?, ?, ?)}",
                    (rank, title, rating, movie_url),
                )

            conn.commit()
            print(f"进度：已完成前 {start_num + 25} 名更新")
            time.sleep(1)
        except Exception as e:
            print(f"爬取第 {start_num} 页失败: {e}")

    # --- 4. 随机推荐逻辑 ---
    print("正在为您抽取今日推荐电影...")
    cursor.execute(
        "SELECT TOP 1 Title, Rating, URL FROM Movies WHERE Rating >= 9.0 ORDER BY NEWID()"
    )
    row = cursor.fetchone()

    if row:
        movie_title, movie_rating, movie_link = row[0], row[1], row[2]
        print("抽取推荐电影已完成！")

        # --- UI 设置 ---
        ctk.set_appearance_mode("dark")
        app = ctk.CTk()
        app.geometry("400x320")
        app.title("🎬 每日电影推荐")
        app.attributes("-topmost", True)

        # 定义点击动作
        def open_url():
            webbrowser.open(movie_link)

        ctk.CTkLabel(
            app, text="今日电影盲盒", font=("Microsoft YaHei", 12), text_color="gray"
        ).pack(pady=(20, 0))

        # 标题做成一个看起来像链接的按钮
        title_btn = ctk.CTkButton(
            app,
            text=f"《{movie_title}》",
            font=("Microsoft YaHei", 24, "bold", "underline"),  # 加上下划线更有链接感
            fg_color="transparent",  # 背景透明
            text_color="#1E90FF",  # 经典的链接蓝
            hover_color="#333333",  # 鼠标悬停变色
            command=open_url,  # 点击打开网页
        )
        title_btn.pack(pady=20)

        ctk.CTkLabel(
            app, text=f"⭐ 评分：{movie_rating}", font=("Microsoft YaHei", 16)
        ).pack(pady=5)
        ctk.CTkLabel(
            app,
            text="(点击标题查看详情)",
            font=("Microsoft YaHei", 10),
            text_color="gray",
        ).pack()

        ctk.CTkButton(
            app, text="我知道了", fg_color="#E50914", command=app.destroy
        ).pack(pady=30)

        app.mainloop()

    conn.close()


if __name__ == "__main__":
    auto_update_and_recommend()
