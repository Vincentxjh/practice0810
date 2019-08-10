#第六个练习 -
bookinfo = [("不一样的卡梅拉", 22.50,120), ("零基础学Android", 65.10,89.80),
            ("摆渡人", 23.40,36.00), ("福尔摩斯探案全集", 22.50,128)]
print("爬取到的秒杀商品信息：\n", bookinfo)
bookinfo.sort(key = lambda x:(x[1], x[1]/x[2]))
print("排序后的商品信息：\n", bookinfo)