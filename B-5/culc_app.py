# 1つの統計量につき専用の関数を実装
# 合計値の出力
def total_calc(num_list):
    # 初期値の設定
    total = 0

    for num in num_list:
        total += num

    return total


# 最大値の出力
def max_calc(num_list):
    max = num_list[0]
    # 1~リストの最後まで処理を繰り返す
    for num in num_list[1:]:
        if num >= max:
            max = num

    return max


# 最小値の出力
def min_calc(num_list):
    min = num_list[0]

    for num in num_list[1:]:
        if num <= min:
            min = num

    return min


# 平均値の出力
def average_calc(num_list):
    total = total_calc(num_list)
    average = total / len(num_list)
    # 小数点第2位までに形式を丸める
    return format(average, ".2f")


# 入力値の受付と演算結果の出力
def main():
    # 入力値の受付
    data = input("データを入力してください(スペース区切り)　>")

    # 空白または数字以外の入力を受け付けた際の処理
    while all(i.isdigit() or i.isspace() for i in data) is False:
        data = input("再度整数または半角スペースを用いて入力してください。　>")

    # int型のリスト化処理
    num_list = [int(i) for i in data.split()]

    # 各計算結果を表示
    print(f"合計値: {total_calc(num_list)}")
    print(f"最大値: {max_calc(num_list)}")
    print(f"最小値: {min_calc(num_list)}")
    print(f"平均値: {average_calc(num_list)}")


# 直接実行時の処理
if __name__ == "__main__":
    main()
