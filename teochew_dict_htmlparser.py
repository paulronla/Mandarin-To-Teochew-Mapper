#coding=utf-8
from html.parser import HTMLParser
from typing import Dict
from re import sub
from html import escape

class Teochew_Dict_HTMLParser(HTMLParser):
    
    def __init__(self):
        super().__init__()
        self._last_starttag = None
        self._last_endtag = None
        self._teochewDict = {}
        self._chineseChar = None
        self._chineseCharEntry = {}
        self._last_listItemKey = None
        self._chaoyinTupleList = []
        self._pinyinList = []
        
    def handle_starttag(self, tag, attrs):
        self._last_starttag = tag

    def handle_endtag(self, tag):
        self._last_endtag = tag

    def handle_data(self, data):
        if self._last_starttag == 'p':
            self._last_starttag = None
            self._chineseChar = data
        
        if self._last_starttag == 'b':
            self._last_starttag = None
            self._last_listItemKey = data

        if self._last_endtag == 'b':
            self._last_endtag = None

            if self._last_listItemKey in ('潮州音：,汕头音：'):
                self._appendChaoyinList(data)
            
            if self._last_listItemKey == '拼    音：':
                self._pinyinList.append(data.strip())
            
            if self._last_listItemKey == '字    义：':
                self._chineseCharEntry = self._processCharDef(data)
                self._teochewDict[self._chineseChar] = self._chineseCharEntry
                self._resetStateForNextChar()

    def feed(self, data):
        escaped = sub('<[^\x00-\xFF]+?>', lambda match: escape(match.group(0)), data)
        super().feed(escaped)
    
    def getTeochewDict(self) -> Dict[str,Dict[str,str]]:
        return self._teochewDict
            
    def _extractChaoyin(self, data: str) -> str:
        chaoyinSplit = data.strip('[ ').split()
        chaoyinSplit[1] = chaoyinSplit[1][chaoyinSplit[1].find(']')+1:]
        parenthesisIndex = chaoyinSplit[1].find('（')

        if self._chaoyinTupleList and '潮' in self._chaoyinTupleList[-1][0] and self._chaoyinTupleList[-1][2] and '汕' in self._last_listItemKey:
            chaoyinSplit[0] += '(汕)'
        
        while ~parenthesisIndex:
            chaoyinSplit[0] += '('+chaoyinSplit[1][parenthesisIndex+1]+')'
            parenthesisIndex = chaoyinSplit[1].find('（',parenthesisIndex+3)
        
        return chaoyinSplit[0]
    
    def _appendChaoyinList(self, data: str) -> None:
        chaoyin = self._extractChaoyin(data)
        self._chaoyinTupleList.append((self._last_listItemKey,chaoyin,self._isValidChaoyin(chaoyin)))
    
    def _isValidChaoyin(self, chaoyin: str) -> bool:
        ans = True

        for suffix in ('iê', 'iou', 'uêg', 'uêng'):
            ans &= suffix not in chaoyin

        return ans

    def _processCharDef(self, entry: str) -> Dict[str,str]:
        entryChunks = entry.split()
        charPinyinChaoyin = {}

        for chunk in entryChunks:
            periodIdx = chunk.find('.')

            if ~periodIdx:
                potentialPinyinChaoyinMapping = chunk[periodIdx+1:]
                potentialPinyinChaoyinMapping = potentialPinyinChaoyinMapping.split('||')
                
                if len(potentialPinyinChaoyinMapping) > 1:
                    pinyin = potentialPinyinChaoyinMapping[0]
                    chaoyinList = potentialPinyinChaoyinMapping[1].split('|')
                else:
                    chaoyinList = potentialPinyinChaoyinMapping[0].split('|')

                for ziyiChaoyin in chaoyinList:
                    for chaoyinTuple in self._chaoyinTupleList:
                        chaoyin = chaoyinTuple[1].split('(')[0]
                        if chaoyin in ziyiChaoyin and chaoyinTuple[2]:
                            newPinyin = self._transformPinyinTone(pinyin)
                            charPinyinChaoyin[newPinyin] = charPinyinChaoyin[newPinyin]+'|'+chaoyinTuple[1] if newPinyin in charPinyinChaoyin else chaoyinTuple[1]
                            break
        
        if not charPinyinChaoyin:
            if len(self._pinyinList) > 1:
                print('Error: More than one pinyin, but no mapping provided for Chinese char: '+ self._chineseChar)
            
            charPinyinChaoyin[self._transformPinyinTone(self._pinyinList[0])] = '|'.join([chaoyinTuple[1] for chaoyinTuple in self._chaoyinTupleList if chaoyinTuple[2]])

        return charPinyinChaoyin

    def _transformPinyinTone(self, pinyin: str) -> str:
        for char in pinyin:
            if ord(char) > 127:
                idx = 'āáǎàēéěèīíǐìōóǒòūúǔù'.find(char)
                if idx < 4:
                    return pinyin.replace(char,'a',1)+str(idx % 4 + 1)
                if idx < 8:
                    return pinyin.replace(char,'e',1)+str(idx % 4 + 1)
                if idx < 12:
                    return pinyin.replace(char,'i',1)+str(idx % 4 + 1)
                if idx < 16:
                    return pinyin.replace(char,'o',1)+str(idx % 4 + 1)
                if idx < 20:
                    return pinyin.replace(char,'u',1)+str(idx % 4 + 1)
        
        return pinyin+'5'
    
    def _resetStateForNextChar(self) -> None:
        self._last_starttag = None
        self._last_endtag = None
        self._chineseChar = None
        self._chineseCharEntry = {}
        self._last_listItemKey = None
        self._chaoyinTupleList = []
        self._pinyinList = []
