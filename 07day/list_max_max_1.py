def list_max_max_1(list=[]):
    """
    返回一个列表中的最大和第二大的数
    :param: list
    :return:
    """
    for j in range(2):
        for i in range(len(list)):   #每次 从 0 下标开始 和后一个 比大小，最大的到最后，这里只需要最大的两个，
            # 所以只需 比两轮
            if i < len(list)-1:
                (list[i], list[i+1]) = (list[i+1], list[i]) if list[i] > list[i+1] else (list[i], list[i+1])

    return list[-2:]#(list[len(list)-1], list[len(list)-2])


list1 = list_max_max_1([9, 1, 2, 3, 7, 4, 6, 8, 5, 1])
print(list1)