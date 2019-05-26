from math import sqrt

num = int(input("请输入一个正整数:"))
end = int(sqrt(num))+1
is_prime = True
for i in range(2,end+1):
    if num % 2 == 0 or num % i == 0:

        is_prime = False
        break

if is_prime and num !=0 :
    print("%d是素数" %num)
else:
    print("%d 不是素数" %num)