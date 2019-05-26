#写一个程序判断输入的正整数是不是回文素数。

if __name__ == '__main__':
    num = int(input("请输入一个正整数："))
    if judge_prime(num) and judge_huiwen(num):
        print("%d 是一个回文素数"%num)
    else:
        print("%d 不是一个回文素数"%num)

