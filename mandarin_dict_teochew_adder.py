from typing import List, Dict, Tuple


def add_teochew_pronunciation(
        line: str, pinyin_chaoyin_dict: Dict[str, Dict[str, str]]
        ) -> Tuple[str, int]:
    word = DictEntry(line)
    pinyin_list = word.get_pinyin_list()
    simp_chinese_chars = word.get_simp_chars()
    valid_simp_chinese_chars = _map_invalid_chars(simp_chinese_chars)
    chaoyin_list = []
    chaoyin_str = '<>'

    if len(pinyin_list) > len(valid_simp_chinese_chars):
        return (line, 0)

    for i,pinyin in enumerate(pinyin_list):
        char = valid_simp_chinese_chars[i]
        pinyin = pinyin.lower()
        
        if char in pinyin_chaoyin_dict:
            pinyin_chaoyin_mapping = pinyin_chaoyin_dict[char]
            
            if pinyin in pinyin_chaoyin_mapping:
                chaoyin = pinyin_chaoyin_mapping[pinyin]
                chaoyin_list.append(chaoyin)

            else:
                chaoyin_list.append('|'.join({chaoyin: None 
                        for chaoyin_group in pinyin_chaoyin_mapping.values() 
                        for chaoyin in chaoyin_group.split('|')
                        }))
        
        else:
            chaoyin_list.append('???')

    for chaoyin in chaoyin_list:
        if chaoyin != '???':
            chaoyin_str = '<' + ' '.join(chaoyin_list) + '>'
            break
    
    return (word.get_trad_chars() 
            + ' ' + simp_chinese_chars + ' [' + ' '.join(pinyin_list) 
            + '] ' + chaoyin_str + word.get_definitions(), 
            len(chaoyin_str))


def _map_invalid_chars(chinese_words: str) -> str:
    ans = []

    for char in chinese_words:
        if char.isdigit():
            ans.append(['〇','一','二','三','四','五','六','七','八','九'][int(char)])
        elif char in '，。？！':
            continue
        else:
            ans.append(char)
    
    return ''.join(ans)


class DictEntry:
    def __init__(self, line: str):
        (self._trad_chars, self._simp_chars, 
            self._pinyin_list, self._definition) = self._process(line)

    def _process(self, line: str) -> Tuple[str, str, List[str], str]:
        beg, bracket, definition = line.partition('] ')
        characters, bracket, pinyin = beg.partition(' [')

        return (*characters.split(), pinyin.split(), definition)

    def get_definitions(self) -> str:
        return self._definition

    def get_simp_chars(self) -> str:
        return self._simp_chars

    def get_pinyin_list(self) -> List[str]:
        return self._pinyin_list

    def get_trad_chars(self) -> str:
        return self._trad_chars