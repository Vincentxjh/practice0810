#第四个练习 - 模拟结账打折功能

def fun_checkout(money):
    '''
    功能：计算商品总金额，并进行打折处理
    :return:
    '''
    summoney = sum(money)
    if 500<= summoney < 1000:
        discount = 0.9
    elif 1000 <= summoney < 2000:
        discount = 0.8
    elif 2000 <= summoney < 3000:
        discount = 0.7
    elif summoney >= 3000:
        discount = 0.6
    else:
        discount = 1
    discountmoney = summoney * discount
    return summoney, discountmoney

#调用函数
print("=========结算金额==========")
money_list = []
while True:
    money = float(input("请输入商品价格（结束请输入0）："))
    if money == 0:
        break
    else:
        money_list.append(money)
checked_money = fun_checkout(money_list)
print("商品总金额为：{:.2f}".format(checked_money[0]), "折后金额为：{:.2f}".format(checked_money[1]))