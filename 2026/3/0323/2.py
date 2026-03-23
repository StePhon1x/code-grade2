import customtkinter as ctk
import webbrowser

# 模拟从数据库拿到的数据
movie_title = "雨中曲"
movie_rating = 9.1
movie_link = "https://movie.douban.com/subject/1293350/"

def show_fancy_popup(title, rating, link):
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
    header_bar = ctk.CTkFrame(app, width=40, height=4, fg_color="#E50914", corner_radius=2)
    header_bar.pack(pady=(20, 10))

    # --- 2. 评分标签 (圆角小胶囊风格) ---
    rating_frame = ctk.CTkFrame(app, fg_color="#333333", corner_radius=20)
    rating_frame.pack(pady=5)
    
    rating_label = ctk.CTkLabel(
        rating_frame, 
        text=f" ★ {rating} ", 
        font=("HarmonyOS Sans SC", 13, "bold"), 
        text_color="#FFD700" # 金色星标
    )
    rating_label.pack(padx=12, pady=2)

    # --- 3. 电影标题 (超大加粗，点击跳转) ---
    def open_url():
        webbrowser.open(link)

    title_btn = ctk.CTkButton(
        app,
        text=title,
        font=("Microsoft YaHei", 32, "bold"),
        fg_color="transparent",
        hover_color="#2A2A2A",
        text_color="#FFFFFF",
        cursor="hand2",
        command=open_url
    )
    title_btn.pack(pady=(20, 10), padx=20)

    # 下方提示语
    hint_label = ctk.CTkLabel(app, text="点击标题探索电影详情", font=("Microsoft YaHei", 11), text_color="#666666")
    hint_label.pack()

    # --- 4. 底部动作按钮 ---
    # 空白占位，撑开间距
    spacer = ctk.CTkLabel(app, text="", height=20)
    spacer.pack()

    # 优雅的线性按钮
    btn_close = ctk.CTkButton(
        app, 
        text="遇见下一部", 
        width=160,
        height=36,
        corner_radius=18,
        fg_color="transparent",
        border_width=1,
        border_color="#E50914",
        text_color="#E50914",
        hover_color="#331111",
        font=("Microsoft YaHei", 13),
        command=app.destroy
    )
    btn_close.pack(pady=10)

    app.mainloop()

# 测试运行
show_fancy_popup(movie_title, movie_rating, movie_link)