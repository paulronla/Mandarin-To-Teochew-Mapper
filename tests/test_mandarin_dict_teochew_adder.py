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