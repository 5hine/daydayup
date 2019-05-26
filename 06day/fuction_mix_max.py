# 实现 实现计算求最大公约数和最小公倍数的函数。
#from math import sqrt
def gcd(x,y):
    (x,y) = (y,x) if x > y else (x ,y)
    for i in range(x,0,-1):
        if y % i == 0 and x % i == 0:
            print("%d 是 %d 和 %d 的 最大公约数"%(i,x,y))
            print("%d 是 %d 和 %d 的 最小公倍数"%(x*y/i,x,y))
            break

# gcd(33,70)
