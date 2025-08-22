# 関数の定義
def beauty_kuku(row_num, column_num):

    # 空白桁の設定
    width_row = len(str(row_num))
    width_column = len(str(column_num))
    width_ans = len(str(row_num * column_num))

    for i in range(1, row_num + 1):
        for j in range(1, column_num + 1):

            # 中央揃えかつ桁に応じて空白を設けて表示するよう設定
            answer = f"{j:<{width_column}} x {i:<{width_row}} = {i*j:>{width_ans}} " + "|"

            # 改行 or 空白に分けて出力
            if j == column_num:
                print(answer)
            else:
                print(answer, end=" ")


# 入力受付
def custom_num():
    row_num = int(input("行数を入力してください: "))
    column_num = int(input("列数を入力してください: "))

    return beauty_kuku(row_num, column_num)


# ファイルが直接実行された際にのみ行う処理
if __name__ == "__main__":
    custom_num()
