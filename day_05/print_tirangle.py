row = int(input("请输入你想要的行数："))
for i in range(row):
    for j in range(row):
        if j<=i:
            print('*',end='')
    print()


for i in range(row):
    for j in range(row,0,-1):
        if j<=i+1:
            print('*',end='')
        else:
            print(' ',end='')
    print('')

for i in range(row):
    for j in range(row, 0, -1):
        if j <= i + 1:
            print('*', end='')
        else:
            print(' ', end='')
    for j in range(row):
        if j <i:
            print('*',end='')
    print('')
