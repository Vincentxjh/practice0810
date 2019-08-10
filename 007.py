#第七个练习 - 根据生日判断星座

def fun_constellation(month, day):
    '''
    功能：根据生日判断星座
    :param month: 月份
    :param day: 日期
    :return: 星座
    '''
    constellation_list = ["水瓶座","双鱼座","白羊座","金牛座","双子座","巨蟹座","狮子座","处女座","天秤座","天蝎座","射手座","摩羯座"]
    day_list = [20,19,21,20,21,22,23,23,23,24,23,22]
    if day_list[month-1] <= day:
        return(constellation_list[month-1])
    else:
        if month == 1:
            month += 12
        return(constellation_list[month-2])
#调用函数
birthday = input("请输入生日（如：0128）：")
month = birthday[0:2]
month.lstrip('0')
day = birthday[2:4]
constellation = fun_constellation(int(month), int(day))
print("您的星座为：", constellation)
