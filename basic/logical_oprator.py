# 論理演算子（logical operators）
# and, or, not

a = 1
b = 1
c = 10
d = 100
print(a == b and c > d) # False
print(a == b or c > d) # True
print(not a == b) # False

# Challenge1
# 年齢が10歳以上かつ身長が110cm以上なら乗れるアトラクション
age = 13
height = 140
print(age >= 10 and height >= 110)

# Challenge2
# 修士号保持もしくは5年以上経験があればVisaの取得が可能
master = False
job_experience = 6
print(master or job_experience >=  5)