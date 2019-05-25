#鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
#5* male + 3 * female + chick / 3  = 100  (文)
#  male + female + chick = 100   (只)
#公鸡数量
male = 0
#母鸡数量
female = 0
#小
chick = 0

for male in range(20):
    for female in range(33):
        chick = 100 - male - female
        if (5* male + 3 * female + chick / 3 == 100):
            print("%d 只公鸡，%d 只母鸡,%d 只小鸡"%(male,female,chick))