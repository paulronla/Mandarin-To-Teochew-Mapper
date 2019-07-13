from html.parser import HTMLParser
from typing import Dict, List
from re import sub
from html import escape


class TeochewDictHTMLParser(HTMLParser):
    
    def __init__(self):
        super().__init__()
        self._start_tag = None
        self._end_tag = None
        self._teochew_dict = {}
        self._chinese_char = None
        self._chinese_char_entry = {}
        self._curr_category = None
        self._chaoyin_tuple_list = []
        self._pinyin_list = []
        
    def handle_starttag(self, tag, attrs):
        self._start_tag = tag

    def handle_endtag(self, tag):
        self._end_tag = tag

    def handle_data(self, data):
        if self._start_tag == 'p':
            self._start_tag = None
            self._chinese_char = data
        
        if self._start_tag == 'b':
            self._start_tag = None
            self._curr_category = data

        if self._end_tag == 'b':
            self._end_tag = None

            if self._curr_category in ('潮州音：,汕头音：'):
                self._append_chaoyin_list(data)
            
            if self._curr_category == '拼    音：':
                self._pinyin_list.append(self._transform_pinyin_tone(data.strip()))
            
            if self._curr_category == '字    义：':
                self._chinese_char_entry = self._process_char_def(data)
                self._teochew_dict[self._chinese_char] = self._chinese_char_entry
                self._reset_state_for_next_char()

    def feed(self, data):
        escaped = sub('<[^\x00-\xFF]+?>', lambda match: escape(match.group(0)), data)
        super().feed(escaped)
    
    def get_teochew_dict(self) -> Dict[str,Dict[str,str]]:
        return self._teochew_dict
            
    def _extract_chaoyin(self, data: str) -> str:
        """ 
        Ex input: [ig4 乙]（又）
        Desired output: ig4(又)

        (汕) is used to indicate a pronunciation that is specific to the 
            prestigious (Shantou) form of the Teochew dialect and not 
            redundant with the Chaozhou spoken variant

        """
        *chaoyin, homophone_and_indicator = data.strip('[ ').split()
        chaoyin = [chaoyin[0]]
        chaoyin_indicator = homophone_and_indicator[homophone_and_indicator.find(']')+1:]

        if self._chaoyin_tuple_list:
            prev_category, prev_chaoyin, prev_chaoyin_is_prestige = self._chaoyin_tuple_list[-1]
            
            if '潮' in prev_category and prev_chaoyin_is_prestige and '汕' in self._curr_category:
                chaoyin.append('(汕)')

        for i, char in enumerate(chaoyin_indicator):
            if char == '）':
                chaoyin.append('(' + chaoyin_indicator[i-1] + ')')
        
        return ''.join(chaoyin)
    
    def _append_chaoyin_list(self, data: str) -> None:
        """SIDE EFFECT: self._chaoyin_tuple_list
        """
        chaoyin = self._extract_chaoyin(data)

        for idx in [idx for idx, chaoyin_tuple in enumerate(self._chaoyin_tuple_list) 
                if chaoyin.split('(')[0] == chaoyin_tuple[1].split('(')[0]]:
            tup = self._chaoyin_tuple_list[idx] 
            self._chaoyin_tuple_list[idx] =  (tup[0], tup[1].replace('(汕)',''), tup[2])
            return
        
        self._chaoyin_tuple_list.append(
            (self._curr_category, chaoyin, self._is_prestige_chaoyin(chaoyin))
        )
    
    def _is_prestige_chaoyin(self, chaoyin: str) -> bool:
        for suffix in ('iê', 'iou', 'uêg', 'uêng'):
            if suffix in chaoyin:
                return False

        return True

    def _process_char_def(self, entry: str) -> Dict[str,str]:
        """
        The explanation portion of each Chinese character potentially gives 
        the mapping between specific pinyins to chaoyins, when there are 
        multiple pinyins and chaoyins.
        """
        char_pinyin_chaoyin_map = {}
        word = []
        chaoyin_list = []
        curr_pinyin = None

        for char in entry:
            char = char.lower()
            if char in {'0','1','2','3','4','5','6','7','8','9',
                    'a','b','c','d','e','f','g','h','i','j','k','l','m',
                    'n','o','p','q','r','s','t','u','v','w','x','y','z',
                    'ā','á','ǎ','à','ē','é','ě','è','ī','í','ǐ','ì','ō',
                    'ó','ǒ','ò','ū','ú','ǔ','ù','ê','ǖ','ǘ','ǚ','ǜ','ü'}:
                word.append(char)
                continue
            
            if self._is_chaoyin(word):
                potential_chaoyin = ''.join(word)
                word = []

                if potential_chaoyin in [chaoyin.split('(')[0] for chaoyin in chaoyin_list]:
                    continue

                for chaoyin_tuple in self._chaoyin_tuple_list:
                    chaoyin_type, chaoyin_with_indicators, chaoyin_is_prestige = chaoyin_tuple
                    chaoyin, *indicators = chaoyin_with_indicators.split('(')

                    if chaoyin == potential_chaoyin and chaoyin_is_prestige:
                        chaoyin_list.append(chaoyin_with_indicators)
                        break

            else:
                potential_pinyin = ''.join(word)

                if not potential_pinyin or potential_pinyin.isdigit():
                    word = []
                    continue

                potential_pinyin = self._transform_pinyin_tone(potential_pinyin)
                word = []

                for pinyin in self._pinyin_list:
                    if pinyin == potential_pinyin:
                        if curr_pinyin and chaoyin_list:
                            char_pinyin_chaoyin_map = self._gen_pinyin_chaoyin_map(
                                                    curr_pinyin, chaoyin_list, 
                                                    char_pinyin_chaoyin_map)
                            
                        curr_pinyin = pinyin
                        chaoyin_list = []
                        break

        if curr_pinyin and chaoyin_list:
            char_pinyin_chaoyin_map = self._gen_pinyin_chaoyin_map(
                                    curr_pinyin, chaoyin_list, 
                                    char_pinyin_chaoyin_map)

        missed_pinyin_list = [pinyin for pinyin in self._pinyin_list 
                            if pinyin not in char_pinyin_chaoyin_map]
        missed_chaoyin_list = [chaoyin_tuple[1] for chaoyin_tuple in self._chaoyin_tuple_list 
                            if chaoyin_tuple[2] and 
                            chaoyin_tuple[1] not in '|'.join(char_pinyin_chaoyin_map.values()).split('|')]

        if missed_pinyin_list and missed_chaoyin_list:
            char_pinyin_chaoyin_map[missed_pinyin_list[0]] = '|'.join(missed_chaoyin_list)

            for i in range(1,len(missed_pinyin_list)):
                char_pinyin_chaoyin_map[missed_pinyin_list[i]] = char_pinyin_chaoyin_map[missed_pinyin_list[0]]
        
        elif missed_pinyin_list:
            char_pinyin_chaoyin_map[missed_pinyin_list[0]] = '|'.join([chaoyin_tuple[1] 
                                                        for chaoyin_tuple in self._chaoyin_tuple_list 
                                                        if chaoyin_tuple[2]])

            for i in range(1,len(missed_pinyin_list)):
                char_pinyin_chaoyin_map[missed_pinyin_list[i]] = char_pinyin_chaoyin_map[missed_pinyin_list[0]]
        
        elif missed_chaoyin_list:
            for chaoyin in missed_chaoyin_list:
                if not char_pinyin_chaoyin_map:
                    char_pinyin_chaoyin_map[''] = chaoyin
                    continue

                for pinyin in char_pinyin_chaoyin_map:
                    char_pinyin_chaoyin_map[pinyin] += '|'+chaoyin

        return char_pinyin_chaoyin_map

    def _gen_pinyin_chaoyin_map(
            self, pinyin: str, chaoyin_list: List[str], 
            char_pinyin_chaoyin_map: Dict[str,str]) -> Dict[str,str]:
        if pinyin in char_pinyin_chaoyin_map:
            for chaoyin in chaoyin_list:
                if chaoyin not in char_pinyin_chaoyin_map[pinyin].split('|'):
                    char_pinyin_chaoyin_map[pinyin] += '|'+chaoyin
        else:
            char_pinyin_chaoyin_map[pinyin] = '|'.join(chaoyin_list)

        return char_pinyin_chaoyin_map

    def _is_chaoyin(self, word: List[str]) -> bool:
        if len(word) < 2:
            return False

        char = word[-1]

        return char > '0' and char < '9' and word[-2].isalpha()

    def _transform_pinyin_tone(self, pinyin: str) -> str:
        """ CE-Dict uses pinyin with tone numbers, not tone markings
        """
        transformed = pinyin

        for char in pinyin:
            if char == 'ü':
                transformed = transformed.replace(char,'u:',1)
                continue

            if ord(char) > 127:
                idx = 'āáǎàēéěèīíǐìōóǒòūúǔùǖǘǚǜ'.find(char)
                if idx < 0:
                    print(pinyin + ' was not transformed correctly')
                    return pinyin
                if idx < 4:
                    return transformed.replace(char,'a',1)+str(idx % 4 + 1)
                if idx < 8:
                    return transformed.replace(char,'e',1)+str(idx % 4 + 1)
                if idx < 12:
                    return transformed.replace(char,'i',1)+str(idx % 4 + 1)
                if idx < 16:
                    return transformed.replace(char,'o',1)+str(idx % 4 + 1)
                if idx < 20:
                    return transformed.replace(char,'u',1)+str(idx % 4 + 1)
                if idx < 24:
                    return transformed.replace(char,'u:',1)+str(idx % 4 + 1)
        
        return transformed+'5'
    
    def _reset_state_for_next_char(self) -> None:
        self._start_tag = None
        self._end_tag = None
        self._chinese_char = None
        self._chinese_char_entry = {}
        self._curr_category = None
        self._chaoyin_tuple_list = []
        self._pinyin_list = []
