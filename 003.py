#第三个练习 - 计算BMI

def fun_bmi(*person):
    '''
    功能：根据身高体重计算BMI
    :param person: 可变参数，需要传递带三个元素的列表，
                   分别是姓名、身高（单位：米）、体重（单位：千克）
    :return:
    '''
    for person_list in person:
        for item in person_list:
            person = item[0]
            height = item[1]
            weight = item[2]
            print("="*13 + person + "="*13)
            print("身高：" + str(height) + "米 \t 体重：" + str(weight) + "千克")
            bmi = weight / (height * height)
            print("您的BMI指数为：" + str(bmi))
            if bmi < 18.5:
                print("您的体重过轻，请增加营养 ～＠_＠～ \n")
            if bmi >= 18.5 and bmi < 24.9:
                print("您的体重在正常范围，请保持 ～＾_＾～ \n")
            if bmi >= 24.9 and bmi < 29.9:
                print("您的体重过重，请注意 ～＠_＠～　\n")
            if bmi >= 29.9:
                print("您的体重超重，请减肥 ～＠_＠～ \n")

#函数调用
list_w = [("绮梦", 1.70, 65), ("零语", 1.78, 50), ("黛兰", 1.72, 66)]
list_m = [("梓轩", 1.80, 75), ("冷伊", 1.75, 70)]
fun_bmi(list_w, list_m)