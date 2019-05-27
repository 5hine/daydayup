def list_max_max_1(list=[]):
    """
    返回一个列表中的最大和第二大的数
    :param: list
    :return:
    """
for j in range(len(list)):
    for i in range(len(list)):

        if i < len(list)-1:
            (list[i], list[i+1]) = (list[i+1], list[i]) if list[i] > list[i+1] else (list[i], list[i+1])

    return (list[len(list)-1], list[len(list)-2])


a,b = list_max_max_1([1, 2, 3, 4, 6, 8, 5])
print(a, b)