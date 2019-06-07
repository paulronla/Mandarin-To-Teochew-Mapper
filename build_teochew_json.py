#coding=utf-8
import json
from teochew_dict_htmlparser import Teochew_Dict_HTMLParser

TEOCHEW_HTML_PATH = '../../teochew_dict_html/'
OUTPUT_DIR = './'
START_PAGE = 0
END_PAGE = 916

parser = Teochew_Dict_HTMLParser()

for page in range(START_PAGE, END_PAGE):
    if page == 2:
        continue

    print('Processing page: ' + str(page))
    
    with open(TEOCHEW_HTML_PATH + str(page) + '.html', 'r', encoding='utf-8') as f:
        html_string = f.read()

    parser.feed(html_string)

with open(OUTPUT_DIR + 'mandarin_teochew.json', 'w', encoding='utf-8') as f:
    json.dump(parser.getTeochewDict(), f, ensure_ascii=False, indent=4)
