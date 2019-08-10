#第八个练习 - 将美元转换为人民币
def fun_moneyconversion(usdollar):
    return(usdollar * 6.28)

dollars = float(input("请输入要转换的美元金额："))
rmb = fun_moneyconversion(dollars)
print("转换后的人民币金额是：{:.2f}".format(rmb))