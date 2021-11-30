# whileループ
# count = 0
# while count < 10:
#     print(count)
#     count += 1

# break と continue
# while True:
#     age  = int(input("あなたは何歳ですか？\n"))
#     if not 0 <= age < 120:
#         print("入力された値は正しくありません")
#         continue
#     else:
#         print(f"あなたは{age}歳です")
#         break

# Challenge1
#「ユーザに年齢を聞き、18歳以上なら入れるカジノを作成する。カジノに入ったらゲームを選べるようにする。選択できるゲームは、
# 1:ルーレット
# 2:ブラックジャック
# 3: ポーカー
# 選択後、ゲーム内容をprint()する」
# 上記のコードを, 1~3以外の文字が入力されたら再度ゲームを選べるようにrefactoringする

age = int(input("年齢はいくつですか？\n"))
casino_age = 18
game_text = """プレイするゲームを転宅してください
1: ルーレット
2: ブラックジャック
3: ポーカー
:
"""
if age >= casino_age:
    print("どうぞお入りください")
    while True:
        game = int(input(game_text))
        if game == 1:
            print("あなたはルーレットを選びました")
            break
        elif game == 2:
            print("あなたはブラックジャックを選びました")
            break
        elif game == 3:
            print("あなたはポーカーを選びました")
            break
        else:
            print("再度ゲームを選んでください")
else:
    print(f"{casino_age}歳未満の方はカジノは入れません")