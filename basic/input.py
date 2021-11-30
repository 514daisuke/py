# input(): ユーザの入力した値（文字列）を取得する
#
# age = input("何歳ですか？")
# print(f"あなたは{age}歳です。")

# Challenge1
# ユーザに年齢を聞き、18歳以上なら入れるカジノを作成する
# ハードコーディングをなくす
# age = int(input("あなたは何歳ですか？\n"))
# casino_age = 18
# if age >= casino_age:
#     print("どうぞお入りください")
# else:
#     print(f"{casino_age}歳未満の方はカジノは入れません")

# Challenge2
# カジノに入ったらゲームを選べるようにする。選択できるゲームは
# 1:ルーレット
# 2:ブラックジャック
# 3:ポーカー
#選択後、ゲームの内容をprint()する


age = int(input("あなたは何歳ですか？\n"))
casino_age = 18
game_text = """プレイするゲームを転宅してください
1: ルーレット
2: ブラックジャック
3: ポーカー
"""
if age >= casino_age:
    print("どうぞお入りください")
    game = input(game_text)
    if game == "1":
        print("あなたはルーレットを選びました")
    elif game == "2":
        print("あなたはブラックジャックを選びました")
    elif game == "3":
        print("あなたはポーカーを選びました")
    else:
        print("1~3を選んでください")
else:
    print(f"{casino_age}歳未満の方はカジノは入れません")