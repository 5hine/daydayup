import random

def play():
    num = random.randint(1, 6) + random.randint(1, 6)
    return num

def choose(i,list=[]):
    print("第%d次掷"%i)
    num = play()
    print("您的点数是：%d"%num)
    if num == 7 or num == 11:
        print("恭喜您，获胜啦！！！")
    elif num == 2 or num == 3 or num == 12:
        print("很遗憾，您输了")
    else:
        list.append(num)
        #print(list)
        if len(list) != len(set(list)):
            print("很遗憾，您输了")
        else:
            i += 1
            choose(i,list)



print("请输入数字（1 为 掷骰子，2为 退出）：")
while True:
    i = 1
    player_list = []
    ctrl = int(input("是否开始骰子："))
    if ctrl == 1:
        num = choose(i,player_list)
    elif ctrl == 2:
        break
    else:
        ctrl = input("你的输入有误，请重新输入")


