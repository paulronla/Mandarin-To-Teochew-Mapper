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
        
        self.assertEquals(addTeochewPronunciation('成熟 成熟 [cheng2 shu2] /mature/ripe/to mature/to ripen/Taiwan pr. [cheng2 shou2]/', pinyinChaoyinDict),'成熟 成熟 [cheng2 shu2] /sêng5(文)|sian5(白)|zian5(白)|cian5 sêg8/mature/ripe/to mature/to ripen/Taiwan pr. [cheng2 shou2]/')