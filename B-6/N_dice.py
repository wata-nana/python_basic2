from random import randint


# 任意のサイコロを振る関数を定義
def dice(N_side, M_count):
    result = list(randint(1, int(N_side)) for i in range(int(M_count)))

    return result


def main():
    # 入力受付
    answer = False
    while answer is False:
        N_side = input("サイコロの面の数は?: ")
        M_count = input("何回振りますか?: ")

        if (N_side.isdigit() and M_count.isdigit()) is False:
            print("再度整数のみを入力してください。")
            answer = False
        else:
            answer = True

    # 結果の出力
    print(dice(N_side, M_count))


# 直接実行時の処理
if __name__ == "__main__":
    main()
