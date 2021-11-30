# in演算子
fruits = ["apple", "peach", "grapes", "banana"]
# print("apple" in fruits)
# print("lemon" in fruits)
# print("lemon" not in fruits)
# print("h" in "hello")

#　Challnge
#　ユーザに好きなフルーツを入力してもらい、そのフルーツがfruitsリストにあればそのフルーツを削除、なければそのフルーツを追加するプログラム
choice_fruits = input("好きなフルーツは？\n")

if choice_fruits in fruits:
    print(f"{choice_fruits}ですね。差し上げます")
    fruits.remove(choice_fruits)

else:
    print(f"{choice_fruits}ですね。仕入れました")
    fruits.append(choice_fruits)

print(f"現在のフルーツは{fruits}になっています")