def main():
    while True:
        n = int(input("Please input n (1<=n<=13): "))
        if 1 <= n <= 13:
            break
        else:
            print("Input range error, please re-enter.")

    c = 1
    for i in range(n, 0, -1):   # 从 n 到 1
        for j in range(1, i + 1):
            if c < 10:
                print(f"0{c}", end="")  # 小于 10 补 0
            else:
                print(c, end="")
            c += 1
        print()  # 换行


if __name__ == "__main__":
    main()
