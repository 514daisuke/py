# forループ
# fruits = ["apple", "peach", "grapes", "banana"]

# for fruit in fruits:
#     print(f"I love {fruit}!!")
#
# for char in "hello wolrd!!":
#     print(f"char:{char}")

# iterationとiterable

# Challenge1
# ユーザに好きなフルーツを入力してもらい、fruitsリストの各フルーツに対して「好き/好きじゃない」をprint()する
# favorite = input("好きなフルーツは？\n")
# for fruit in fruits:
#     if fruit == favorite:
#         print(f"I love {fruit}!!")
#     else:
#         print(f"{fruit}は好きじゃない")

# Challenge2
# fruitsリストの各フルーツに対して「好き / 好きじゃない」をユーザに聞いて、好きなフルーツリスト、好きじゃないフルーツリストを作成する
favorite_fruit = []
normal_fruits = []

fruits = ["apple", "peach", "grapes", "banana"]
for fruit in fruits:
    choice = input(f"{fruit}は好き？ y/n\n")

    if choice == "y":
        favorite_fruit.append(fruit)
    else:
        normal_fruits.append(fruit)

print(f"favarite fruits: {favorite_fruit}")
print(f"normal fruits: {normal_fruits}")