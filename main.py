#!/usr/bin/python
# -*- coding: utf-8 -*-
#####################################
# File name : main.py
# Create date : 2019-08-18 14:38
# Modified date : 2019-08-18 14:42
# Author : DARREN
# Describe : not set
# Email : lzygzh@126.com
#####################################
from __future__ import division
from __future__ import print_function

from causality_extract import CausalityExractor

def test_content(content):
    extractor = CausalityExractor()
    datas = extractor.extract_main(content)
    for data in datas:
        print('******'*4)
        print('cause', ''.join([word.split('/')[0] for word in data['cause'].split(' ') if word.split('/')[0]]))
        print('tag', data['tag'])
        print('effect', ''.join([word.split('/')[0] for word in data['effect'].split(' ') if word.split('/')[0]]))

'''测试'''

def test():
    content1 = """
    截至2008年9月18日12时，5·12汶川地震共造成69227人死亡，374643人受伤，17923人失踪，是中华人民共和国成立以来破坏力最大的地震，也是唐山大地震后伤亡最严重的一次地震。
    """
    test_content(content1)

    content2 = '''
    2015年1月4日下午3时39分左右，贵州省遵义市习水县二郎乡遵赤高速二郎乡往仁怀市方向路段发生山体滑坡，发生规模约10万立方米,导致多辆车被埋，造成交通双向中断。此事故引起贵州省委、省政府的高度重视，省长陈敏尔作出指示，要求迅速组织开展救援工作，千方百计实施救援，减少人员伤亡和财物损失。遵义市立即启动应急救援预案，市应急办、公安、交通、卫生等救援力量赶赴现场救援。目前，灾害已造成3人遇难1人受伤，一辆轿车被埋。
    当地时间2010年1月12日16时53分，加勒比岛国海地发生里氏7.3级大地震。震中距首都太子港仅16公里，这个国家的心脏几成一片废墟，25万人在这场骇人的灾难中丧生。此次地震中的遇难者有联合国驻海地维和部队人员，其中包括8名中国维和人员。虽然国际社会在灾后纷纷向海地提供援助，但由于尸体处理不当导致饮用水源受到污染，灾民喝了受污染的水后引发霍乱，已致至少2500多人死亡。
    '''
    test_content(content2)

    content3 = '''
    American Eagle 四季度符合预期 华尔街对其毛利率不满导致股价大跌
    我之所以考试没及格，是因为我没有好好学习。
    因为天晴了，所以我今天晒被子。
    因为下雪了，所以路上的行人很少。
    我没有去上课是因为我病了。
    因为早上没吃的缘故，所以今天还没到放学我就饿了.
    因为小华身体不舒服，所以她没上课间操。
    因为我昨晚没睡好，所以今天感觉很疲倦。
    因为李明学习刻苦，所以其成绩一直很优秀。
    雨水之所以不能把石块滴穿，是因为它没有专一的目标，也不能持之以恒。
    他之所以成绩不好，是因为他平时不努力学习。
    你之所以提这个问题，是因为你没有学好关联词的用法。
    减了税,因此怨声也少些了。
    他的话引得大家都笑了，室内的空气因此轻松了很多。
    他努力学习，因此通过了考试。
    既然明天要下雨，就不要再出去玩。
    既然他还是那么固执，就不要过多的与他辩论。
    既然别人的事与你无关，你就不要再去过多的干涉。
    既然梦想实现不了，就换一个你自己喜欢的梦想吧。
    既然别人需要你，你就去尽力的帮助别人。
    既然生命突显不出价值，就去追求自己想要的生活吧。
    既然别人不尊重你，就不要尊重别人。 因果复句造句
    既然题目难做，就不要用太多的时间去想，问一问他人也许会更好。
    既然我们是学生，就要遵守学生的基本规范。
    '''
    test_content(content3)

#   extractor = CausalityExractor()
#   datas = extractor.extract_main(content1)
#   for data in datas:
#       print('******'*4)
#       print('cause', ''.join([word.split('/')[0] for word in data['cause'].split(' ') if word.split('/')[0]]))
#       print('tag', data['tag'])
#       print('effect', ''.join([word.split('/')[0] for word in data['effect'].split(' ') if word.split('/')[0]]))

def run():
    test()

run()

