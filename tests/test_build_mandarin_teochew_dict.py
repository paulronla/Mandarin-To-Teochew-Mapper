#coding=utf-8
import sys
sys.path.append('../')
import unittest
from build_mandarin_teochew_dict import idxLineToDict, updateIdxDict, idxDictToString

class Test_Build_Mandarin_Teochew_Dict(unittest.TestCase):
    def test_idxLineToDict(self):
        idxDict = idxLineToDict('了,307962,308048,4837355,4837423', {})
        self.assertEqual(idxDict, {'了': [307962,308048,4837355,4837423]})
        idxDict = idxLineToDict('一下,9792', idxDict)
        self.assertEqual(idxDict, {'了': [307962,308048,4837355,4837423], '一下': [9792]})
        idxDict = idxLineToDict('倒數,568206,568344', idxDict)
        self.assertEqual(idxDict, {'了': [307962,308048,4837355,4837423], '一下': [9792], '倒數': [568206,568344]})

    def test_updateIdxDict(self):
        oldIdxDict = {'成熟': [2729817], '美國': [5356318], '倒數': [568206,568344]}
        newIdxDict = {key:[] for key in oldIdxDict}
        runningCnt = 0

        dictTuple = updateIdxDict('倒數', oldIdxDict, newIdxDict, runningCnt)
        runningCnt += 10
        self.assertEqual(dictTuple, ({'成熟': [2729817], '美國': [5356318], '倒數': [568344]}, {'成熟': [], '美國': [], '倒數': [568206]}))
        
        dictTuple = updateIdxDict('成熟', oldIdxDict, newIdxDict, runningCnt)
        self.assertEqual(dictTuple, ({'美國': [5356318], '倒數': [568344]}, {'成熟': [2729827], '美國': [], '倒數': [568206]}))
        runningCnt += 38
        
        dictTuple = updateIdxDict('倒數', oldIdxDict, newIdxDict, runningCnt)
        self.assertEqual(dictTuple, ({'美國': [5356318]}, {'成熟': [2729827], '美國': [], '倒數': [568206,568392]}))

    def test_idxDictToString(self):
        self.assertEqual(idxDictToString({'成熟': [2729827], '美國': [], '倒數': [568206,568392]}), '成熟,2729827\n美國,\n倒數,568206,568392\n')
        

