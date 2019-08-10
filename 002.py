#第二个练习 - 利用函数计算BMI
def fun_bmi(person, height, weight):
    '''
    功能：根据身高、体重计算BMI指数
    person: 姓名
    heigth: 身体，单位：米
    weigth: 体重，单位：千克
    '''
    print(person + "的身高为：" + str(height) + "米\t体重：" + str(weight) + "千克")
    # 计算BMI，并显示
    bmi = weight / (height * height)
    print("您的BMI指数为：" + str(bmi))

    # 根据BMI判断身材是否合理
    if bmi < 18.5:
        print("您的体重过轻，请增加营养 ～＠_＠～ \n")
    if bmi >= 18.5 and bmi < 24.9:
        print("您的体重在正常范围，请保持 ～＾_＾～ \n")
    if bmi >= 24.9 and bmi < 29.9:
        print("您的体重过重，请注意 ～＠_＠～　\n")
    if bmi >= 29.9:
        print("您的体重超重，请减肥 ～＠_＠～ \n")

#调用函数
fun_bmi("路人甲", 1.83, 66)
fun_bmi("路人乙", 1.70, 88)