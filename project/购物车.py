#####购物车
good_list = []
while True:
    sallary = input("输入你的工资：\n")
    if sallary.isdigit():
        sallary = int(sallary)
        break
    else:
        print("输入错误！请重新输入……\n\n")
print("如需退出，请按:\033[1;32m q \033[0m".center(80))
while True:
    goods = [{"name":"电脑","price":5000},
             {"name":"鼠标","price":50},
             {"name":"游艇","price":50000},
             {"name":"美女","price":5}
             ]
    for i,j in enumerate(goods):
        print(i+1,j["name"],j["price"])

    good = input("请选择需要购买的商品编号：")
    if good.isdigit() and 0 < int(good) <= len(goods):
        good = int(good)
        if goods[good-1]["price"] > sallary:
            print("\n\033[1;31m余额不足！\033[0m 请重新选择……\n")
            continue
        else:
            good_list.append(goods[good - 1])
            sallary -= goods[good - 1]["price"]
    elif good == "q" or good == "Q":
        for i,j in enumerate(good_list):
            print(i+1,j["name"])
        print("余额为：%s" % sallary)
        break
    else:
        print("\n\033[1;31m选择错误，请重新选择商品编号。\033[0m\n")
        continue

