# 関数の定義
def kuku_custom():
    # 入力受付
    row_num = int(input("行数を入力してください: "))
    column_num = int(input("列数を入力してください: "))

    # 繰り返し処理
    for i in range(1, row_num+1):
        for j in range(1, column_num+1):

            if j == column_num:
                print(i*j)

            else:
                print(i*j, end=" ")


# ファイルを直接実行した際にのみ行う処理
if __name__ == "__main__":
    kuku_custom()
