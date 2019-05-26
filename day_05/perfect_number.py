# 第一个完全数是6，它有约(因)数1、2、3、6，除去它本身6外，其余3个数相加，1+2+3=6。
for i in range(2,100):
    sum = 1
    for j in range(2,100):
        if j < i and i % j == 0:
            sum += j
    if sum == i:
        print("%d 是完美数"%i)