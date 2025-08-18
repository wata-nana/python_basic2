# 関数の定義
def kuku():
    # かけられる数の設定
    for i in range(1, 10):
        # かける数の設定
        for j in range(1, 10):

            # かける数が9の時に改行する
            if j == 9:
                print(i*j)

            # その他は一文字開ける
            else:
                print(i*j, end=" ")


# ファイルを直接実行した際にのみ行う処理
if __name__ == "__main__":
    kuku()
