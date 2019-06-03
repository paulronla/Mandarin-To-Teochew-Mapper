import json
from html.parser import HTMLParser

class TeochewHTMLParser(HTMLParser):
    
    def __init__(self):
        super().__init__()
        self.last_starttag = None
        self.last_endtag = None
        self.teochewDict = {}
        self.chineseChar = None
        self.chineseCharEntry = {}
        self.last_listItemKey = None
        self.chaoyinList = []
        

    def handle_starttag(self, tag, attrs):
        self.last_starttag = tag

    def handle_endtag(self, tag):
        self.last_endtag = tag

    def handle_data(self, data):
        if self.last_starttag == 'p':
            self.chineseChar = data
        
        if self.last_starttag == 'b':
            self.last_listItemKey = data

        if self.last_endtag == 'b':
            if self.last_listItemKey in ('潮州音：,汕头音：'):
                self.appendChaoyinList(data)
            
            if self.last_listItemKey == '拼    音：':
                print('do some more logic here')
            
            if self.last_listItemKey == '字    义：':
                print('run some other method here')
            
    def extractChaoyin(self, data: str) -> str:
        chaoyinSplit = data.strip('[ ').split()
        parenthesisIndex = chaoyinSplit[1].find('（')
        
        while ~parenthesisIndex:
            chaoyinSplit[0] += '('+chaoyinSplit[1][parenthesisIndex+1]+')'
            parenthesisIndex = chaoyinSplit[1].find('（',parenthesisIndex+3)
        
        return chaoyinSplit[0]
    
    def appendChaoyinList(self, chaoyin: str) -> None:
        self.chaoyinList.append((self.last_listItemKey,chaoyin,self.isValidChaoyin(chaoyin)))
    
    def isValidChaoyin(self, chaoyin: str) -> bool:
        return ('iê', 'iou', 'uêg', 'uêng') not in chaoyin


parser = TeochewHTMLParser()
print(parser.extractChaoyin('[dion1 场1]（白）（姓）'))


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

