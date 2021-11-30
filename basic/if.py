# if文

age = -20
age_alcohol = 21
if age >= age_alcohol:
    print("You can drink beer!")
else:
    print("You are too young to drink beer")

age_drive = 18
if age >= age_alcohol:
    print("You can drink beer!")
elif age < age_drive:
    print("You cannot even drive!")
else:
    print("You are not allowed to drink beer but you can drive only if You have a driver's license")

if not 0 < age < 120:
    print("The value is invalid!!")

#Challenge1
#もしbalance(残高)がwithdraw(引き出し額)より大きければ、balanceを更新し、そうでなければ引き出せないATMを作る
balance = 3000000
withdrawal = 130000000

# if balance > withdrawal:
#     balance = balance - withdrawal
#     #balance -= withdrawal
#     print(f"Your new balance is {balance}")
# else:
#     print("You don't have money!!")

#Challenge2
#Challenge1に加えて、引き出し学の上限を100万に設定し、上限を超えて引き出そうとすると引き出せないATMを作る
withdrawal_limit = 1000000

if withdrawal > withdrawal_limit:
    print(f"The withdrawal limit is {withdrawal_limit}")
elif balance > withdrawal:
    balance -= withdrawal
    print(f"Your new balance is {balance}")
else:
    print("You cannot withdraw!!")