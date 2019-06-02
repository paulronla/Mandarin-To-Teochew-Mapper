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
        

    def handle_starttag(self, tag, attrs):
        self.last_starttag = tag

    def handle_endtag(self, tag):
        self.last_endtag = tag

    def handle_data(self, data):
        if self.last_starttag == 'p':
            self.chineseChar = data
        
        if self.last_starttag == 'b':
            if data in ('潮州音：', '汕头音：', '拼    音：', '字    义：' ):
                self.last_listItemKey = data
            
            
        


parser = TeochewHTMLParser()



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

