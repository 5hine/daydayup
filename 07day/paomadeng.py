# 在屏幕上显示跑马灯文字效果
import os
import time

def main():
    content = "红红火火恍恍惚惚"
    while True:
        #清理屏幕的输出
        os.system('clear')
        print(content)
        #休眠0.2s
        time.sleep(0.2)
        content = content[1:] + content[0]

if __name__ == '__main__':
    main()
