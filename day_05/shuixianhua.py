from math import pow
hundreds = 0
tens = 0
units = 0
# print(int(7.3),int(7.6))    7 7   直接省去小数
for i in range(100,1000):
    hundreds = int(i % 1000 / 100)
    tens = int(i % 100 / 10)
    units = i % 10
    if i == (pow(hundreds,3)+pow(tens,3)+pow(units,3)):
        print("%d 是水仙花数" %i)