import requests
from bs4 import BeautifulSoup
import pyodbc
import time
import customtkinter as ctk
import webbrowser


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

        ctk.set_appearance_mode("dark")

    app = ctk.CTk()
    app.title("")  # 隐藏标题文字，更简洁
    app.geometry("400x320")
    app.resizable(False, False)

    # 让窗口居中并置顶
    app.attributes("-topmost", True)

    # 背景颜色 (高级炭灰)
    app.configure(fg_color="#1A1A1A")

    # --- 1. 顶部小装饰 ---
    header_bar = ctk.CTkFrame(
        app, width=40, height=4, fg_color="#E50914", corner_radius=2
    )
    header_bar.pack(pady=(20, 10))

    # --- 2. 评分标签 (圆角小胶囊风格) ---
    rating_frame = ctk.CTkFrame(app, fg_color="#333333", corner_radius=20)
    rating_frame.pack(pady=5)

    rating_label = ctk.CTkLabel(
        rating_frame,
        text=f" ★ {movie_rating} ",
        font=("HarmonyOS Sans SC", 13, "bold"),
        text_color="#FFD700",  # 金色星标
    )
    rating_label.pack(padx=12, pady=2)

    # --- 3. 电影标题 (超大加粗，点击跳转) ---
    def open_url():
        webbrowser.open(movie_link)

    title_btn = ctk.CTkButton(
        app,
        text=movie_title,
        font=("Microsoft YaHei", 32, "bold"),
        fg_color="transparent",
        hover_color="#2A2A2A",
        text_color="#FFFFFF",
        cursor="hand2",
        command=open_url,
    )
    title_btn.pack(pady=(20, 10), padx=20)

    # 下方提示语
    hint_label = ctk.CTkLabel(
        app,
        text="点击标题探索电影详情",
        font=("Microsoft YaHei", 11),
        text_color="#666666",
    )
    hint_label.pack()

    # --- 4. 底部动作按钮 ---
    # 空白占位，撑开间距
    spacer = ctk.CTkLabel(app, text="", height=20)
    spacer.pack()

    # 优雅的线性按钮
    btn_close = ctk.CTkButton(
        app,
        text="我知道了",
        width=160,
        height=36,
        corner_radius=18,
        fg_color="transparent",
        border_width=1,
        border_color="#E50914",
        text_color="#E50914",
        hover_color="#331111",
        font=("Microsoft YaHei", 13),
        command=app.destroy,
    )
    btn_close.pack(pady=10)

    app.mainloop()

    conn.close()


if __name__ == "__main__":
    auto_update_and_recommend()
