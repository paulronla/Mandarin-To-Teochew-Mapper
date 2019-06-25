import json
from teochew_dict_htmlparser import TeochewDictHTMLParser

TEOCHEW_HTML_PATH = '../../teochew_dict_html/'
OUTPUT_DIR = './'
START_PAGE = 0
END_PAGE = 916

parser = TeochewDictHTMLParser()

for page in range(START_PAGE, END_PAGE):
    if page == 2: # page 2 pulled from their database is always a duplicate of page 1
        continue

    print('Processing page: ' + str(page))
    
    with open(TEOCHEW_HTML_PATH + str(page) + '.html', 'r', encoding='utf-8') as f:
        html_string = f.read()

    parser.feed(html_string)

with open(OUTPUT_DIR + 'mandarin_teochew.json', 'w', encoding='utf-8') as f:
    json.dump(parser.get_teochew_dict(), f, ensure_ascii=False, indent=4)
