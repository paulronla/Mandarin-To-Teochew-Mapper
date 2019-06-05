import json
from html.parser import HTMLParser
from typing import Dict

class TeochewHTMLParser(HTMLParser):
    
    def __init__(self):
        super().__init__()
        self.last_starttag = None
        self.last_endtag = None
        self.teochewDict = {}
        self.chineseChar = None
        self.chineseCharEntry = {}
        self.last_listItemKey = None
        self.chaoyinTupleList = []
        self.pinyinList = []
        

    def handle_starttag(self, tag, attrs):
        self.last_starttag = tag

    def handle_endtag(self, tag):
        self.last_endtag = tag

    def handle_data(self, data):
        if self.last_starttag == 'p':
            self.last_starttag = None
            self.chineseChar = data
        
        if self.last_starttag == 'b':
            self.last_starttag = None
            self.last_listItemKey = data

        if self.last_endtag == 'b':
            self.last_endtag = None

            if self.last_listItemKey in ('潮州音：,汕头音：'):
                self.appendChaoyinList(data)
            
            if self.last_listItemKey == '拼    音：':
                self.pinyinList.append(data.strip())
            
            if self.last_listItemKey == '字    义：':
                self.chineseCharEntry = self.processCharDef(data)
                self.teochewDict[self.chineseChar] = self.chineseCharEntry
                self.resetStateForNextChar()
            
    def extractChaoyin(self, data: str) -> str:
        chaoyinSplit = data.strip('[ ').split()
        chaoyinSplit[1] = chaoyinSplit[1][chaoyinSplit[1].find(']')+1:]
        parenthesisIndex = chaoyinSplit[1].find('（')

        if self.chaoyinTupleList and '潮' in self.chaoyinTupleList[-1][0] and self.chaoyinTupleList[-1][2]:
            chaoyinSplit[0] += '(汕)'
        
        while ~parenthesisIndex:
            chaoyinSplit[0] += '('+chaoyinSplit[1][parenthesisIndex+1]+')'
            parenthesisIndex = chaoyinSplit[1].find('（',parenthesisIndex+3)
        
        return chaoyinSplit[0]
    
    def appendChaoyinList(self, data: str) -> None:
        chaoyin = self.extractChaoyin(data)
        self.chaoyinTupleList.append((self.last_listItemKey,chaoyin,self.isValidChaoyin(chaoyin)))
    
    def isValidChaoyin(self, chaoyin: str) -> bool:
        ans = True

        for suffix in ('iê', 'iou', 'uêg', 'uêng'):
            ans &= suffix not in chaoyin

        return ans

    def processCharDef(self, entry: str) -> Dict[str,str]:
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
                    for chaoyinTuple in self.chaoyinTupleList:
                        chaoyin = chaoyinTuple[1].split('(')[0]
                        if chaoyin in ziyiChaoyin and chaoyinTuple[2]:
                            charPinyinChaoyin[self.transformPinyinTone(pinyin)] += '|'+chaoyin if pinyin in charPinyinChaoyin else chaoyin
                            break
        
        if not charPinyinChaoyin:
            if len(self.pinyinList) > 1:
                print('Error: More than one pinyin, but no mapping provided for Chinese char: '+ self.chineseChar)
            
            charPinyinChaoyin[self.transformPinyinTone(self.pinyinList[0])] = '|'.join([chaoyinTuple[1] for chaoyinTuple in self.chaoyinTupleList if chaoyinTuple[2]])

        return charPinyinChaoyin

    def transformPinyinTone(self, pinyin: str) -> str:
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
    
    def resetStateForNextChar(self) -> None:
        self.last_starttag = None
        self.last_endtag = None
        self.chineseChar = None
        self.chineseCharEntry = {}
        self.last_listItemKey = None
        self.chaoyinTupleList = []
        self.pinyinList = []

parser = TeochewHTMLParser()
#print(parser.extractChaoyin('[dion1 场1]（白）（姓）'))
#print(parser.isValidChaoyin('[huêg4 场1]（白）（姓）'))
parser.feed('''<dl>
                <dt>
                  <p>〇</p>	
                </dt>
                <dd><ul>
  	    
 		            <li><b>潮州音：</b>[lêng5 零]
 		  <button class="laba" role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/czh/83B141DF-5FB6-4E89-9C94-38BA6A4EBD56.mp3" ></button>
     
     </li>
 		
 		            <li><b>拼    音：</b>líng  <button class="laba2"  role='dict_audio_js'
     data-rel="http://sound.file.czyzd.com/pth/2EE9A9EC-FA55-44BF-915F-0F5CFA992FEE.mp3"></button></li>
 		
                    <li><b>字    义：</b>数的空位，同“零”，多用于书面语中：三~六号|一九七~年。</li>
                    
                </ul>
                </dd>
             </dl>''')
print(json.dumps(parser.teochewDict,ensure_ascii=False,indent=4))
#print(parser.chineseCharEntry)


#teochewDict = {
#	"一": {
#		"yi1": "zêg8|ig4|iao1"
#	},
#	"弹": {
#		"dan4": "tang5",
#		"tan2": "tang5|duan7"
#	}
#}

#with open('teochewDict.json', 'w', encoding='utf-8') as f:
#    json.dump(teochewDict, f, ensure_ascii=False, indent=4)

#with open('teochewDict.json', 'r', encoding='utf-8') as f:
#    teochewDict = json.load(f)

#print(teochewDict['弹']['tan2'])


