#coding=utf-8
from typing import List, Dict, Tuple

def addTeochewPronunciation(line: str, pinyinChaoyinDict: Dict[str, Dict[str,str]]) -> str:
    word = DictEntry(line)
    pinyinList = word.getPinyinList()
    simpChineseChars = word.getSimpChars()
    chaoyinList = []

    for i,pinyin in enumerate(pinyinList):
        chaoyin = pinyinChaoyinDict[simpChineseChars[i]][pinyin]
        chaoyinList.append(chaoyin)
    
    return word.getTradChars() + ' ' + simpChineseChars + ' [' + ' '.join(pinyinList) + '] /' + ' '.join(chaoyinList) + word.getDefinitions()

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