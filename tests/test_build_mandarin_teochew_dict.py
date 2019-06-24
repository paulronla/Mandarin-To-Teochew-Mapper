import sys
sys.path.append('../')
import unittest
from build_mandarin_teochew_dict import idx_line_to_dict, update_idx_dict, idx_dict_to_string

class TestBuildMandarinTeochewDict(unittest.TestCase):
    def test_idx_line_to_dict(self):
        idx_dict = idx_line_to_dict('了,307962,308048,4837355,4837423', {})
        self.assertEqual(idx_dict, {'了': [307962,308048,4837355,4837423]})
        idx_dict = idx_line_to_dict('一下,9792', idx_dict)
        self.assertEqual(idx_dict, {
                '了': [307962,308048,4837355,4837423], '一下': [9792]})
        idx_dict = idx_line_to_dict('倒數,568206,568344', idx_dict)
        self.assertEqual(idx_dict, {
                '了': [307962,308048,4837355,4837423], '一下': [9792], 
                '倒數': [568206,568344]})

    def test_update_idx_dict(self):
        old_idx_dict = {'成熟': [2729817], '美國': [5356318], 
                '倒數': [568206,568344]}
        new_idx_dict = {key:[] for key in old_idx_dict}
        running_cnt_extra_chars = 0

        dict_tuple = update_idx_dict(
                '倒數', old_idx_dict, new_idx_dict, running_cnt_extra_chars)
        running_cnt_extra_chars += 10
        self.assertEqual(dict_tuple, (
                {'成熟': [2729817], '美國': [5356318], '倒數': [568344]}, 
                {'成熟': [], '美國': [], '倒數': [568206]}))
        
        dict_tuple = update_idx_dict(
                '成熟', old_idx_dict, new_idx_dict, running_cnt_extra_chars)
        self.assertEqual(dict_tuple, (
                {'美國': [5356318], '倒數': [568344]}, 
                {'成熟': [2729827], '美國': [], '倒數': [568206]}))
        running_cnt_extra_chars += 38
        
        dict_tuple = update_idx_dict(
                '倒數', old_idx_dict, new_idx_dict, running_cnt_extra_chars)
        self.assertEqual(dict_tuple, (
                {'美國': [5356318]}, 
                {'成熟': [2729827], '美國': [], '倒數': [568206,568392]}))

    def test_idx_dict_to_string(self):
        self.assertEqual(idx_dict_to_string(
            {'成熟': [2729827], '美國': [], '倒數': [568206,568392]}), 
            '成熟,2729827\n美國,\n倒數,568206,568392\n')
        

