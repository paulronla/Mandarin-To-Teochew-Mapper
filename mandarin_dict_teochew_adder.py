#coding=utf-8
from typing import List, Dict, Tuple

def addTeochewPronunciation(line: str, pinyinChaoyinDict: Dict[str, Dict[str,str]]) -> str:
    word = DictEntry(line)
    pinyinList = word.getPinyinList()
    simpChineseChars = word.getSimpChars()
    validSimpChineseChars = _mapInvalidChars(simpChineseChars)
    chaoyinList = []
    chaoyinStr = ''

    for i,pinyin in enumerate(pinyinList):
        char = validSimpChineseChars[i]
        pinyin = pinyin.lower()
        
        if char in pinyinChaoyinDict:
            pinyinChaoyinMapping = pinyinChaoyinDict[char]
            
            if pinyin in pinyinChaoyinMapping:
                chaoyin = pinyinChaoyinMapping[pinyin]
                chaoyinList.append(chaoyin)

            else:
                chaoyinList.append('|'.join({chaoyin:None for chaoyinGroup in pinyinChaoyinMapping.values() for chaoyin in chaoyinGroup.split('|')}))
        
        else:
            chaoyinList.append('???')

    for chaoyin in chaoyinList:
        if chaoyin != '???':
            chaoyinStr = '/' + ' '.join(chaoyinList)
            break
    
    return word.getTradChars() + ' ' + simpChineseChars + ' [' + ' '.join(pinyinList) + '] ' + chaoyinStr + word.getDefinitions()

def _mapInvalidChars(chineseWords: str) -> str:
    ans = []

    for char in chineseWords:
        if char.isdigit():
            ans.append(['〇','一','二','三','四','五','六','七','八','九'][ord(char)-48])
        elif char in '，。？！':
            continue
        else:
            ans.append(char)
    
    return ''.join(ans)

class DictEntry:
    def __init__(self, line: str):
        self._tradChars, self._simpChars, self._pinyinList, self._definition = self._process(line)

    def _process(self, line: str) -> Tuple[str,str,List[str],str]:
        beg, bracket, definition = line.partition('] ')
        characters, bracket, pinyin = beg.partition(' [')

        return (*characters.split(), pinyin.split(), definition)

    def getDefinitions(self) -> str:
        return self._definition

    def getSimpChars(self) -> str:
        return self._simpChars

    def getPinyinList(self) -> List[str]:
        return self._pinyinList

    def getTradChars(self) -> str:
        return self._tradChars