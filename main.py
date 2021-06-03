def isint(s):  # 整数値を表しているかどうかを判定
    try:
        int(s, 10)  # 文字列を実際にint関数で変換してみる
    except ValueError:
        return False
    else:
        return True

data = input("数値を入力してください。")

if(isint(data)):
    is_same_num = False
    for num in range(len(data)-1):
        is_same_num = True
        if bool(num == 0 and data[num] == "0") or data[num] != data[num+1]:
            is_same_num = False
            break

    if(is_same_num):
        print("入力された数値はぞろ目です。")
    else:
        print("入力された数値はぞろ目ではありません。")
else:
    print("数値以外が入力されています。")