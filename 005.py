#第五个练习 - 全局变量和局部变量应用

tree = "我只是一颗松树"
def fun_dream():
    tree = "孩子们为我挂上了彩灯、礼物……我变成了一颗圣诞树 ^_^ \n"
    print(tree)
#调用函数
print("下雪了……\n")
print("========进入了梦乡========\n")
fun_dream()
print("==========梦醒了==========\n")
print(tree)