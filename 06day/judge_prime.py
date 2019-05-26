#练习3：实现判断一个 数是不是素数的函数。
from math import sqrt
def judge_prime(num):
    a = sqrt(num)
    is_prime = True
    for i in range(2,int(sqrt(num))+1):
        if num % i == 0:
            is_prime = False
            break
        else:
            is_prime = True
    return is_prime
# num = int(input("请输入你需要判断的数："))
# if judge_prime(num):
#     print("%d 是素数"%num)
# else:
#     print("%d 不是素数"%num)
