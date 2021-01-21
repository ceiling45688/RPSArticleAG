#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, re
import random

a = input("Enter A:")
b = input("Enter B:")
text = [
        "一想到这是自己的老公就心里美滋滋的。",
        "b突然轻轻的在a的耳旁说道：啵啵",
        "a发出一声猪叫，害羞地说：啵啵",
        "a那被天使吻过的脸庞上无声地滑落了两滴五彩斑斓的泪水，"
        "b赶忙用自己56厘米臂围的大手环抱住了a，哄道：啵啵",
        "b看到a的模样，忍不住笑出了90分贝的猪叫。",
        "b牵起了a的手，虔诚地说 b 唯爱 a，啵啵",
        "a嘴巴嘟嘟，嘟嘟嘟嘟嘟，撒娇道：cnm那你还有那么多cp！啵啵",
        "b不再说话，直接用舌头反复拍打a的嘴唇。",
        "a一愣，害羞地说道：啵啵",
        "b见状，赶快讨好老婆，说：啵啵",
        "a打开了自拍软件，自言自语道：啵啵",
        ]

snh_saying = ["能不能让想睡觉的人睡觉啊！",
              "全深圳的墙不都是一样的吗？",
              "真是REAL一朵白莲。",
              "有锤就放，一堆小丑!",
              "我都看笑出声了。",
              "难顶。",
              "这事整的多尴尬啊。",
              "是不是以为大家看不到她真正的面皮呀，就可以为所欲为？",
              "都是好姐妹。",
              "烂话题，就像默默地闻到有人放了一个屁。",
              "清者自清。",
              "敲里老母。",
              "我的眼泪需要高级纸巾触碰。",
              "你在神气什么？",
              "你在做梦呢？大姐。",
              "不知道有家室的前辈不能碰吗？"
              ]

def newparagraph():
    str = " "
    str += "\r\n" #回车+换行
    # str += "    "
    return str


def sentances():
    str = snh_saying[random.randint(0, len(snh_saying) - 1)]
    return str


for i in a:
    tmp = str()#tmp就是文章
    while len(tmp) < 500 :
        fork = random.randint(0, 20)
        if fork < 5:
            tmp += newparagraph()
        else:
            tmp += text[random.randint(0,len(text) - 1)]
    tmp = tmp.replace("a",a)
    tmp = tmp.replace("b",b)
    tmp = tmp.replace("啵啵", snh_saying[random.randint(0, len(snh_saying) - 1)])
    print(tmp)