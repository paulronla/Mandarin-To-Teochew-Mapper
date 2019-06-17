#coding=utf-8
import sys
sys.path.append('../')
import unittest
import json
from mandarin_dict_teochew_adder import addTeochewPronunciation

MANDARIN_TEOCHEW_JSON_PATH = '../'

class Test_Mandarin_Dict_Teochew_Adder(unittest.TestCase):
    def test_addTeochewPronunciation(self):
        with open(MANDARIN_TEOCHEW_JSON_PATH + 'mandarin_teochew.json', 'r', encoding='utf-8') as fp:
            pinyinChaoyinDict = json.load(fp)
        
        self.assertEqual(addTeochewPronunciation('成熟 成熟 [cheng2 shu2] /mature/ripe/to mature/to ripen/Taiwan pr. [cheng2 shou2]/', pinyinChaoyinDict),'成熟 成熟 [cheng2 shu2] /sêng5(文)|sian5(白)|zian5(白)|cian5 sêg8/mature/ripe/to mature/to ripen/Taiwan pr. [cheng2 shou2]/')
        self.assertEqual(addTeochewPronunciation('美國 美国 [Mei3 guo2] /United States/USA/US/', pinyinChaoyinDict), '美國 美国 [Mei3 guo2] /mui2|bhuê2 gog4/United States/USA/US/')
        self.assertEqual(addTeochewPronunciation('半個 半个 [ban4 ge5] /half of sth/', pinyinChaoyinDict), '半個 半个 [ban4 ge5] /buan3 gai5|go6|gai7/half of sth/')
        self.assertEqual(addTeochewPronunciation('502膠 502胶 [wu3 ling2 er4 jiao1] /cyanoacrylate glue/', pinyinChaoyinDict), '502膠 502胶 [wu3 ling2 er4 jiao1] /ngou6(白)|ngou2|u2(文)|u5 lêng5 no6(训)|ri6 ga1/cyanoacrylate glue/')
        self.assertEqual(addTeochewPronunciation("不怕慢，就怕站 不怕慢，就怕站 [bu4 pa4 man4 jiu4 pa4 zhan4] /it's better to make slow progress than no progress at all (proverb)/", pinyinChaoyinDict), "不怕慢，就怕站 不怕慢，就怕站 [bu4 pa4 man4 jiu4 pa4 zhan4] /bug4 pan3 mang7|bhuang6 ziu6 pan3 zam6/it's better to make slow progress than no progress at all (proverb)/")
        self.assertEqual(addTeochewPronunciation('〻 〻 [xx5] /iteration mark (used to represent a duplicated character)/', pinyinChaoyinDict), '〻 〻 [xx5] /iteration mark (used to represent a duplicated character)/')