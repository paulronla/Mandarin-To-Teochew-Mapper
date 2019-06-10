#coding=utf-8
from html.parser import HTMLParser
from typing import Dict, List
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
                self._pinyinList.append(self._transformPinyinTone(data.strip()))
            
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
        self._chaoyinTupleList.append((self._last_listItemKey,chaoyin,self._isPrestigeChaoyin(chaoyin)))
    
    def _isPrestigeChaoyin(self, chaoyin: str) -> bool:
        for suffix in ('iê', 'iou', 'uêg', 'uêng'):
            if suffix in chaoyin:
                return False

        return True

    def _processCharDef(self, entry: str) -> Dict[str,str]:
        charPinyinChaoyin = {}
        word = []
        chaoyinList = []
        currPinyin = None

        for char in entry:
            char = char.lower()
            if char in {'0','1','2','3','4','5','6','7','8','9',
                'a','b','c','d','e','f','g','h','i','j','k','l','m',
                'n','o','p','q','r','s','t','u','v','w','x','y','z',
                'ā','á','ǎ','à','ē','é','ě','è','ī','í','ǐ','ì','ō',
                'ó','ǒ','ò','ū','ú','ǔ','ù','ê'}:
                word.append(char)
                continue

            elif len(word) < 2:
                word = []
                continue
            
            if self._isChaoyin(word):
                potentialChaoyin = ''.join(word)
                word = []

                if potentialChaoyin in [chaoyin.split('(')[0] for chaoyin in chaoyinList]:
                    continue

                for chaoyinTuple in self._chaoyinTupleList:
                    chaoyin = chaoyinTuple[1].split('(')[0]

                    if chaoyin == potentialChaoyin and chaoyinTuple[2]:
                        chaoyinList.append(chaoyinTuple[1])
                        break

            else:
                potentialPinyin = ''.join(word)
                potentialPinyin = self._transformPinyinTone(potentialPinyin)
                word = []

                for pinyin in self._pinyinList:
                    if pinyin in potentialPinyin:
                        if currPinyin and chaoyinList:
                            charPinyinChaoyin = self._generatePinyinChaoyinMapping(currPinyin, chaoyinList, charPinyinChaoyin)
                            
                        currPinyin = pinyin
                        chaoyinList = []

        if currPinyin and chaoyinList:
            charPinyinChaoyin = self._generatePinyinChaoyinMapping(currPinyin, chaoyinList, charPinyinChaoyin)

        missedPinyinList = [pinyin for pinyin in self._pinyinList if pinyin not in charPinyinChaoyin]
        missedChaoyinList = [chaoyinTuple[1] for chaoyinTuple in self._chaoyinTupleList if chaoyinTuple[2] and chaoyinTuple[1] not in set('|'.join(charPinyinChaoyin.values()).split('|'))]

        if missedPinyinList and missedChaoyinList:
            charPinyinChaoyin[missedPinyinList[0]] = '|'.join(missedChaoyinList)

            for i in range(1,len(missedPinyinList)):
                charPinyinChaoyin[missedPinyinList[i]] = charPinyinChaoyin[missedPinyinList[0]]
        
        elif missedPinyinList:
            charPinyinChaoyin[missedPinyinList[0]] = '|'.join([chaoyinTuple[1] for chaoyinTuple in self._chaoyinTupleList if chaoyinTuple[2]])

            for i in range(1,len(missedPinyinList)):
                charPinyinChaoyin[missedPinyinList[i]] = charPinyinChaoyin[missedPinyinList[0]]
        
        elif missedChaoyinList:
            for chaoyin in missedChaoyinList:
                if not charPinyinChaoyin:
                    charPinyinChaoyin[''] = chaoyin
                    continue

                for pinyin in charPinyinChaoyin:
                    charPinyinChaoyin[pinyin] += '|'+chaoyin

        return charPinyinChaoyin

    def _generatePinyinChaoyinMapping(self, pinyin: str, chaoyinList: List[str], charPinyinChaoyin: Dict[str,str]) -> Dict[str,str]:
        if pinyin in charPinyinChaoyin:
            for chaoyin in chaoyinList:
                if chaoyin not in charPinyinChaoyin[pinyin]:
                    charPinyinChaoyin[pinyin] += '|'+chaoyin
        else:
            charPinyinChaoyin[pinyin] = '|'.join(chaoyinList)

        return charPinyinChaoyin

    def _isChaoyin(self, word: List[str]) -> bool:
        char = word[-1]

        if char > '0' and char < '9' and word[-2].isalpha:
            return True
        
        return False

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
