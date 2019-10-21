import sys
sys.path.append('modules/')
sys.path.append('../modules/')
from mandarin_dict_teochew_adder import add_teochew_pronunciation
import json
from typing import Dict, List

MANDARIN_TEOCHEW_JSON_PATH = 'json/'
IDX_DICT_PATH = ''
MANDARIN_TEOCHEW_DICT_PATH = ''

def _read_idx_to_dict(filename: str) -> Dict[str, List[int]]:
    idx_dict = {}

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            idx_dict = idx_line_to_dict(line, idx_dict)

    return idx_dict

def _write_dict_to_idx(filename: str, idx_dict_str: str) -> None:
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(idx_dict_str)

def idx_line_to_dict(line: str, idx_dict: Dict[str, List[int]]) -> Dict[
        str, List[int]]:
    key, *val = line.rstrip().split(',')
    val = [int(idx) for idx in val]
    idx_dict[key] = val
    
    return idx_dict

def _write_mandarin_teochew_dict(
        filename_with_path: str, pinyin_chaoyin_dict: Dict[str, Dict[str, str]], 
        idx_dict: Dict[str, List[int]]) -> Dict[str, List[int]]:
    *filepath, filename  = filename_with_path.replace('\\', '/').rsplit('/', 1)
    filepath = filepath[0] if filepath else ''
    new_idx_dict = {key:[] for key in idx_dict}
    running_extra_chars = 0
    
    with open(filepath + '/' + filename, 'r', encoding='utf-8') as read_fp:
        with open(filepath + '/' + 'new_' + filename, 'w', 
                encoding='utf-8') as write_fp:
            for line in read_fp:
                if line.startswith('#'):
                    write_fp.write(line)
                else:
                    new_line, extra_char_cnt = add_teochew_pronunciation(
                                            line, pinyin_chaoyin_dict)
                    trad_char, simp_char, *rest = new_line.split()
                    
                    idx_dict, new_idx_dict = update_idx_dict(
                                trad_char, idx_dict, new_idx_dict, running_extra_chars)
                    
                    if trad_char != simp_char:
                        idx_dict, new_idx_dict = update_idx_dict(
                                simp_char, idx_dict, new_idx_dict, running_extra_chars)
                    
                    running_extra_chars += extra_char_cnt
                    write_fp.write(new_line)
            
    return idx_dict_to_string(new_idx_dict)

def update_idx_dict(word: str, old_dict: Dict[str, List[int]], 
                    new_dict: Dict[str, List[int]], 
                    running_extra_chars_cnt: int) \
                    -> (Dict[str, List[int]], Dict[str, List[int]]):
    idx_list = old_dict[word]
                
    if len(idx_list) > 1:
        idx = idx_list.pop(0)
    else:
        idx, = old_dict.pop(word, None)
                
    idx += running_extra_chars_cnt
    new_dict[word].append(idx)

    return (old_dict, new_dict)

def idx_dict_to_string(idx_dict: Dict[str, List[int]]) -> str:
    idx_string_builder = []

    for key, idx_list in idx_dict.items():
        idx_string_builder.append(key + ',' 
                + ','.join([str(idx) for idx in idx_list]) + '\n')
    
    return ''.join(idx_string_builder)

if __name__ == '__main__':
    with open(MANDARIN_TEOCHEW_JSON_PATH + 'mandarin_teochew.json', 'r', 
            encoding='utf-8') as f:
        pinyin_chaoyin_dict = json.load(f)
    
    idx_dict = _read_idx_to_dict(IDX_DICT_PATH + 'cedict.idx')
    new_idx_dict_string = _write_mandarin_teochew_dict(MANDARIN_TEOCHEW_DICT_PATH 
            + 'cedict_ts.u8', pinyin_chaoyin_dict, idx_dict)
    _write_dict_to_idx(IDX_DICT_PATH + 'new_cedict.idx', new_idx_dict_string)
