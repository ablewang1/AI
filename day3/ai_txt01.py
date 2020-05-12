print("\033[1;36mWecome to AI study.Now,let's go!\033[0m\n\n".center(120))
def day3():
    score = 0
    error_list = []
    ##
    print(" \033[1;35mNumber One\033[0m ".center(40,"*"))
    system = input("What is your system?")
    if system.strip()[:7] == "Windows" or system.strip()[:7] == "windows":
        print("I always use it! It is Windows10 ,但是要用\033[1;31m专业版\033[0m哦\n")
    elif system == "Linux" or system == "linux":
        print("\033[1;36m你离大神越来越近了！\033[0m")
    elif system == "Mac" or system == "mac":
        print("\033[1,33m土豪，我们做朋友吧！\033[0m")
    else:
        print("这是国产的操作系统吗？加油，要多多支持国产。")


    ## y = f(x,w)
    print("数学公式【y = f(x,w)】中，各个字母的含义?")
    answer = input("y:")
    if answer == "输出":
        score += 1
        print("right")
    else:
        print("\033[1;31merror\033[0m the right is:输出")

    answer = input("f:")
    if answer == "输出":
        score += 1
        print("right")
    else:
        print("\033[1;31merror\033[0m the right is:输出")

    ##
    print(" \033[1;35mNumber Two\033[0m ".center(40,"*"))

    GPU = input("你电脑配置显卡了吗？[y/n]")
    if GPU == "y":
        print("恭喜你，你可以使用cuda进行并行运算，核心数越多相当于同时工作的人越多")
    elif GPU == "n":
        print('''没有关系，你同样可以使用并行运算，
                 cpu是几核的就相当于几个人同时工作。
                 公司电脑为大家提供的是\033[1;31m英伟达1050Ti4G\033[0m
                 的显卡，欢迎大家多多使用，以后也会给大家提供
                 \033[1;32m云端\033[0m ：\033[33m阿里云GPU服务器\033[0m''')
    else:
        print("非法输入……")


    ##
    print(" \033[1;35mNumber Three\033[0m ".center(40,"*"))
    print("你怎么处理错误呢？要记住：\033[1;31merror\033[0m是必须处理的，\033[1;33mwarning\033[0m可以选择性处理")


    ##
    print(" \033[1;35mNumber Four\033[0m ".center(40,"*"))
    print("你是怎么使用Git工具的？来测一测 文件【test】，哈希值【666】")


    answer = input("初始化本地库")
    if answer == "git init":
        score += 1
        print("you are right")
    else:
        print("\033[1;31merror\033[0m,right is :git init")

    answer = input("创建用户：wa")
    answer1 = input("添加邮箱：1@2")
    if answer == "git config --global user.name wa" and answer1 == "git config --global user.email 1@2":
        score += 2
        print("you are right")
    elif answer == "git config --global user.name wa":
        score += 1
        print("email not true.The right:git config --global user.email 1@2")
    elif answer1 == "git config --global user.email 1@2":
        score += 1
        print("user not True.The right :git config --global user.name wa")
    else:
        print("\033[1;31merror\033[0m,right is :git config --global user.name wa /n git config --global user.email 1@2")


    answer = input("将工作区的“新建/修改”添加到暂存区")
    if answer == "git add test" or answer == "git add *.*":
        score += 1
        print("you are right")
    else:
        print("\033[1;31merror\033[0m,right is :git add test")

    answer = input("将文件从暂存区到本地库,备注：Hi")
    if answer == 'git commit -m "Hi" test':
        score += 1
        print("you are right")
    else:
        print('\033[1;31merror\033[0m,right is :git commit -m "Hi" test')

    answer = input("查看log")
    if answer == 'git log' or answer == 'git reflog':
        score += 1
        print("you are right")
    else:
        print('\033[1;31merror\033[0m,right is :git log')

    answer = input("切回到之前版本：版本哈希值为：666")
    if answer == 'git reset --hard 666':
        score += 1
        print("you are right")
    else:
        print('\033[1;31merror\033[0m,right is :git reset --hard 666')

    answer = input(r"连接到github项目：https://github.com/ablewang1/AI.git 取别名：good")
    if answer == 'git remote add good https://github.com/ablewang1/AI.git':
        score += 1
        print("you are right")
    else:
        print(r'\033[1;31merror\033[0m,right is :git remote add good https://github.com/ablewang1/AI.git')

    answer = input("将master 推到云端 good")
    if answer == 'git push good master':
        score += 1
        print("you are right")
    else:
        print('\033[1;31merror\033[0m,right is :git push good master')

    answer = input("从云端 good 拉取数据到 master")
    if answer == 'git pull good master':
        score += 1
        print("you are right")
    else:
        print('\033[1;31merror\033[0m,right is :git pull good master')

    answer = input("查看连接的github的地址")
    if answer == 'git remote -v' or answer == 'git remote -V':
        score += 1
        print("you are right")
    else:
        print('\033[1;31merror\033[0m,right is :git remote -v')
    print("END ,your score is %d" % score)


    ##
    print(" \033[1;35mNumber Five\033[0m ".center(40,"*"))
    print("AI公司有三种分类，每一类中都有哪些呢？")

    answer = input("第一类：")
    if "deepmind" in answer.split(" "):
        score += 1
        print("deepmind is true")
    if "OpenAI" in answer.split(" "):
        score += 1
        print("OpenAI is true")
    if "NVIDIA" in answer.split(" "):
        score += 1
        print("NVIDIA is true")


    answer = input("第二类将理论变成了现实，有哪些呢：")
    if "Google" in answer.split(" "):
        score += 1
        print("Google is right")
    else:
        print("loss Google \033[1;31error\033[0m")

    if "微软" in answer.split(" "):
        score += 1
        print("微软 is right")
    else:
        print("loss 微软 \033[1;31error\033[0m")

    if "Facebook" in answer.split(" "):
        score += 1
        print("Facebook is right")
    else:
        print("loss Facebook \033[1;31error\033[0m")

    if "百度" in answer.split(" "):
        score += 1
        print("百度 is right")
    else:
        print("loss 百度 \033[1;31error\033[0m")

    if "达摩院" in answer.split(" "):
        score += 1
        print("达摩院 is right")
    else:
        print("loss 达摩院 \033[1;31error\033[0m")


    answer = input("第三类商业化了的公司有哪些呢？")
    if "商汤" in answer.split(" "):
        score += 1
        print("商汤 is right")
    else:
        print("\033[1;31error\033[0m loss 商汤 ")

    if "旷世" in answer.split(" "):
        score += 1
        print("旷世 is right")
    else:
        print("\033[1;31error\033[0m loss 旷世")

    if "云虫" in answer.split(" "):
        score += 1
        print("云虫 is right")
    else:
        print("\033[1;31error\033[0m loss 云虫 ")

    ##
    print(" \033[1;35mNumber Six\033[0m ".center(40,"*"))

    answer = input("计算机之父是谁呢？")
    if answer == "冯诺依曼":
        score += 1
        print('Right')
    else:
        print('\033[1;31merror\033[0m,right is :冯诺依曼')

    answer = input("人工智能之父是谁呢？")
    if answer == "图灵":
        score += 1
        print('Right')
    else:
        print('\033[1;31merror\033[0m,right is :图灵')

    answer = input("深度学习之父是谁呢？")
    if answer == "Hinton":
        score += 1
        print('Right')
    else:
        print('\033[1;31merror\033[0m,right is :Hinton')

    answer = input("谁通过了图灵测试呢？")
    if answer == "GPT2":
        score += 1
        print('Right')
    else:
        print('\033[1;31merror\033[0m,right is :GPT2')


    ##
    print(" \033[1;35mNumber seven\033[0m ".center(40,"*"))
    from PIL import Image

    print("AI的起起伏伏")
    img = Image.open(U"图片\\ai0.png")
    img.show()


    ##
    print(" \033[1;35mNumber eight\033[0m ".center(40,"*"))
    answer = input("AI分类中的学派类有哪些呢？")
    difference = set(["符号主义", "连接主义", "行为主义"]) - set(answer.split(" "))
    difference1 = set(answer.split(" ")) - set(["符号主义", "连接主义", "行为主义"])
    if len(difference) == 0 and len(difference1) == 0:
        score += 3
        print("Great")

    elif len(difference) == 0 and len(difference1) != 0:
        score += 3
        print("Not bad")
        print("多余部分：%s" % difference1)

    elif len(difference) == 2:
        score += 2
        print("缺失部分：%s" % difference)
        print("多余部分：%s" % difference1)
    elif len(difference) == 1:
        score += 1
        print("缺失部分：%s" % difference)
        print("多余部分：%s" % difference1)
    else:
        print("Terrible,your answer has no right")
        print("the right is :%s" % (["符号主义", "连接主义", "行为主义"]))



    ##
    print(" \033[1;35mNumber nine\033[0m ".center(40,"*"))
    answer = input("AI分类中按能力分类有哪些呢？")
    difference = set(["弱人工智能", "强人工智能", "超人工智能"]) - set(answer.split(" "))
    difference1 = set(answer.split(" ")) - set(["弱人工智能", "强人工智能", "超人工智能"])
    if len(difference) == 0 and len(difference1) == 0:
        score += 3
        print("Great")

    elif len(difference) == 0 and len(difference1) != 0:
        score += 3
        print("Not bad")
        print("多余部分：%s" % difference1)

    elif len(difference) == 2:
        score += 1
        print("缺失部分：%s" % difference)
        print("多余部分：%s" % difference1)
    elif len(difference) == 1:
        score += 2
        print("缺失部分：%s" % difference)
        print("多余部分：%s" % difference1)
    else:
        print("Terrible,your answer has no right")
        print("the right is :%s" % (["弱人工智能","强人工智能","超人工智能"]))


    #######
    answer = input("AI分类中按业务领域分类有哪些呢？")
    difference = set(["信号领域", "图像领域", "语音领域", "自然语义", "自动化"]) - set(answer.split(" "))
    difference1 = set(answer.split(" ")) - set(["信号领域", "图像领域", "语音领域", "自然语义", "自动化"])
    if len(difference) == 0 and len(difference1) == 0:
        score += 5
        print("Great")

    elif len(difference) == 0 and len(difference1) != 0:
        score += 5
        print("Not bad")
        print("多余部分：%s" % difference1)

    elif len(difference) == 4:
        score += 1
        print("缺失部分：%s" % difference)
        print("多余部分：%s" % difference1)

    elif len(difference) == 3:
        score += 2
        print("缺失部分：%s" % difference)
        print("多余部分：%s" % difference1)

    elif len(difference) == 2:
        score += 3
        print("缺失部分：%s" % difference)
        print("多余部分：%s" % difference1)

    elif len(difference) == 1:
        score += 4
        print("缺失部分：%s" % difference)
        print("多余部分：%s" % difference1)

    else:
        print("Terrible,your answer has no right")
        print("the right is :%s" % (["信号领域", "图像领域", "语音领域", "自然语义", "自动化"]))


    ##
    print(" \033[1;35mNumber ten\033[0m ".center(40,"*"))
    answer = input("AI分类中按学习方式分类有哪些呢？")
    difference = set(["有监督学习", "无监督学习", "半监督学习", "自监督学习"]) - set(answer.split(" "))
    difference1 = set(answer.split(" ")) - set(["有监督学习", "无监督学习", "半监督学习", "自监督学习"])
    if len(difference) == 0 and len(difference1) == 0:
        score += 4
        print("Great")

    elif len(difference) == 0 and len(difference1) != 0:
        score += 4
        print("Not bad")
        print("多余部分：%s" % difference1)

    elif len(difference) == 3:
        score += 1
        print("缺失部分：%s" % difference)
        print("多余部分：%s" % difference1)

    elif len(difference) == 2:
        score += 2
        print("缺失部分：%s" % difference)
        print("多余部分：%s" % difference1)

    elif len(difference) == 1:
        score += 3
        print("缺失部分：%s" % difference)
        print("多余部分：%s" % difference1)

    else:
        print("Terrible,your answer has no right")
        print("the right is :%s" % (["有监督学习", "无监督学习", "半监督学习", "自监督学习"]))


    ##
    print(" \033[1;35mNumber eleven\033[0m ".center(40,"*"))
    answer = input("AI分类中按实时来分类有哪些呢？")
    difference = set(["在线学习", "离线学习"]) - set(answer.split(" "))
    difference1 = set(answer.split(" ")) - set(["在线学习", "离线学习"])
    if len(difference) == 0 and len(difference1) == 0:
        score += 2
        print("Great")
        print("在线学习是学习和使用同时进行")

    elif len(difference) == 0 and len(difference1) != 0:
        score += 2
        print("Not bad")
        print("多余部分：%s" % difference1)

    elif len(difference) == 1:
        score += 1
        print("缺失部分：%s" % difference)
        print("多余部分：%s" % difference1)

    else:
        print("Terrible,your answer has no right")
        print("the right is :%s" % (["在线学习", "离线学习"]))



    ##
    print(" \033[1;35mNumber twelve\033[0m ".center(40,"*"))
    answer = input("AI分类中按学习步骤来分类有哪些呢？")
    difference = set(["非端到端学习", "端到端学习"]) - set(answer.split(" "))
    difference1 = set(answer.split(" ")) - set(["非端到端学习", "端到端学习"])
    if len(difference) == 0 and len(difference1) == 0:
        score += 2
        print("Great")

    elif len(difference) == 0 and len(difference1) != 0:
        score += 2
        print("Not bad")
        print("多余部分：%s" % difference1)

    elif len(difference) == 1:
        score += 1
        print("缺失部分：%s" % difference)
        print("多余部分：%s" % difference1)

    else:
        print("Terrible,your answer has no right")
        print("the right is :%s" % (["非端到端学习", "端到端学习"]))


    ##
    print(" \033[1;35mNumber thirteen\033[0m ".center(40,"*"))
    answer = input("AI分类中按学习技巧分类有哪些呢？")
    difference = set(["迁移学习", "元学习", "级联学习", "递增学习", "对抗学习", "合作学习"]) - set(answer.split(" "))
    difference1 = set(answer.split(" ")) - set(["迁移学习", "元学习", "级联学习", "递增学习", "对抗学习", "合作学习"])
    if len(difference) == 0 and len(difference1) == 0:
        score += 6
        print("Great")

    elif len(difference) == 0 and len(difference1) != 0:
        score += 6
        print("Not bad")
        print("多余部分：%s" % difference1)

    elif len(difference) == 5:
        score += 1
        print("缺失部分：%s" % difference)
        print("多余部分：%s" % difference1)

    elif len(difference) == 4:
        score += 2
        print("缺失部分：%s" % difference)
        print("多余部分：%s" % difference1)

    elif len(difference) == 3:
        score += 3
        print("缺失部分：%s" % difference)
        print("多余部分：%s" % difference1)

    elif len(difference) == 2:
        score += 4
        print("缺失部分：%s" % difference)
        print("多余部分：%s" % difference1)

    elif len(difference) == 1:
        score += 5
        print("缺失部分：%s" % difference)
        print("多余部分：%s" % difference1)

    else:
        print("Terrible,your answer has no right")
        print("the right is :%s" % (["迁移学习", "元学习", "级联学习", "递增学习", "对抗学习", "合作学习"]))


    ####
    print(" \033[1;35mNumber fourteen\033[0m ".center(40,"*"))
    answer = input("AI分类中按任务来分类有哪些呢？")
    difference = set(["回归", "聚类"]) - set(answer.split(" "))
    difference1 = set(answer.split(" ")) - set(["回归", "聚类"])
    if len(difference) == 0 and len(difference1) == 0:
        score += 2
        print("Great")

    elif len(difference) == 0 and len(difference1) != 0:
        score += 2
        print("Not bad")
        print("多余部分：%s" % difference1)

    elif len(difference) == 1:
        score += 1
        print("缺失部分：%s" % difference)
        print("多余部分：%s" % difference1)

    else:
        print("Terrible,your answer has no right")
        print("the right is :%s" % (["回归", "聚类"]))

    print(score)
    return score

if __name__ == '__main__':
    day3()
