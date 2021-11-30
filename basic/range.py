# range(start, stop, step)
# for i in [1, 2, 3, 4, 5, 6]:

# for i in range(1, 7):
#     print(i)
#
# for i in range(7):
#     print(i)
#
# for i in range(4, 13 ,2):
#     print(i)
# for _ in range(10):
#     print("hello")

# Challenge
# FizzBuzzゲームを作ろう!
# 1~50の数字をそれぞれprint()して、３の倍数で「Fizz」5の倍数で[Buzz]、3と５の倍数で「FizzBuzz」とprint()する

for i in range(1, 51):
    #print(i)
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)