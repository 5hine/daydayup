#打印杨辉三角



#第一种  生成器
# def triangles():
#     L = [1]
#     S = []
#     j = 0
#     while True:
#         yield L

#         L = [1] + S + [1]
#         S = []
#         for i in range(len(L)-1):
#             S.append(L[i] + L[i+1])
#         j += 1
#
#
#第二种   极简
def triangles():
    L = [1]
    while True:
        print(L)
        yield L
        L = [sum(i) for i in zip([0]+L, L+[0])]   # 如：0,1,2,1  1，2,1,0  zip() === 返回zip对象 （0,1),(1,2),(2,1),(1,0)）

a = triangles()
next(a)
next(a)
next(a)
next(a)
next(a)
