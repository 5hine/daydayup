strs = input("请输入你需要检验的文件名：")


def return_suffix(filename):
    """
    获取文件的后缀名
    :param filename:
    :return:string
    """
    pos = filename.rfind('.')
    if pos == -1 or pos == len(filename)-1:
        return filename+"该文件没有后缀名"
    if 0 < pos < len(filename)-1:
        return filename+"的后缀名是"+filename[pos+1:]


print(return_suffix(strs))
