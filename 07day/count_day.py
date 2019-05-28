import calendar

def count_day(strc=""):
    sum = 0
    year_index = strc.find(".")
    day_index = strc.rfind(".")
    if year_index == 4 and day_index == 7:
        year = int(strc[0:year_index])
        day = int(strc[day_index+1:])
        month = int(strc[year_index+1:day_index])
        isleap = calendar.isleap(year)
        list = [31,28,31,30,31,30,31,31,30,31,30,31]
        if isleap:
            list[1] += 1
        for i in range(month-1):
            sum += list[i]
        sum += day
        return (sum,year,strc)
    else:
        print("您输入的日期有误！请严格按照格式输入")


sum,year,strc = count_day(input("请输入你需要计算的年月(如：1990.01.01)："))
print("%s 是 %d 年的第%d天"%(strc, year, sum))