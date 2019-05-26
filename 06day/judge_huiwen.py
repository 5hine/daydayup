#练习2：实现判断一个数是不是回文数的函数。
#101  三位


def judge(num):
    num_str = str(num)
    length = len(num_str)
    isTrue = False
    i = 0
    while i < length/2:
        if num_str[i] == num_str[length-1-i]:
            isTrue = True
        else:
            isTrue = False
        if i+1 == length - i-1 or i+1 == int(length/2):
            return isTrue
        i += 1

# number = 43134
# if judge(number):
#     print("%d 是回文数"%number)
# else:
#     print("%d 不是回文数"%number)

#另一种方法
# def is_palindrome(num):
#     temp = num
#     total = 0           # total  保存 从个位  取到 最高位,在判断相等
#     while temp > 0:
#         total = total * 10 + temp % 10
#         temp //= 10
#     return total == num

