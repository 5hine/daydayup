# 设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成。
import random


def verification_code(length):
    strs = ""
    num = 0
    for i in range(length):
        num = random.randint(65, 122)
        if 91 < num < 97:
            num += 10

        cmd = random.randint(0, 1)
        if cmd == 0:
            aplha = chr(random.randint(48, 57))
        elif cmd == 1:
            aplha = chr(num)

        strs += aplha
    return strs


# for i in range(65, 122):
#     print(chr(i), i)

print(verification_code(10))
