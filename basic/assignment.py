# 変数への代入: assingment
# pythonは snake_case
# クラスはCamelCase
a = "Hello World"

hello = "konnichiwa"
world = "sekai"

# print(hello + b)
print("konnichiwa" + "sekai") #ハードコーディング

# format
"hello{}".format("world")
# 出力：hello world
print("{} {}".format(hello, world))
# 出力：konnichiwa sekai

name = "John"
print("Hey, {}!! How are you doing?".format(name))

balance  = 100
print("balance: {}".format(balance))

# fstring
print(f"{hello} {world}")
print(f"Hey, {name}!! How are you doing?")
print(f"balance: {balance}")