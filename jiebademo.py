# -*- coding: utf-8 -*-
import jieba

rawtext = "夏日熱辣辣 吃西瓜消暑解渴 夏日熱辣辣 喝一杯凍檸檬茶 夏日熱辣辣 你要喝楊枝甘露 夏日熱辣辣 他要喝珍珠奶茶"
rawtext = unicode(rawtext, 'utf-8')
seg_list = jieba.cut(rawtext)
print " ".join(seg_list)

