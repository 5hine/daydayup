"""定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法。"""
from math import sqrt

class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move_to(self, x, y):
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        self.x += dx
        self.y += dy

    def get(self):
        print("该点的坐标为%d和%d"%(self.x, self.y))

    def get_distinct(self, another):
        return sqrt((self.x-another.x)**2+(self.y-another.y)**2)


if __name__ == "__main__":
    point1 = Point(1,5)
    point2 = Point(5,6)
    point1.get()
    point1.move_by(5,6)
    point1.get()
    point1.move_to(0, 0)
    print("这两点的位移是", point1.get_distinct(point2))
