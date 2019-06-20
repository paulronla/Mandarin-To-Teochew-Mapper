#coding=utf-8
from mandarin_dict_teochew_adder import addTeochewPronunciation
import json
from typing import Dict, List

MANDARIN_TEOCHEW_JSON_PATH = ''
IDX_DICT_PATH = ''
MANDARIN_TEOCHEW_DICT_PATH = ''

def _readIdxToDict(filename: str) -> Dict[str, List[int]]:
    idxDict = {}

    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            idxDict = idxLineToDict(line, idxDict)

    return idxDict

def _writeDictToIdx(filename: str, idxDictStr: str) -> None:
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(idxDictStr)

def idxLineToDict(line: str, idxDict: Dict[str, List[int]]) -> Dict[str, List[int]]:
    key, *val = line.rstrip().split(',')
    val = [int(idx) for idx in val]
    idxDict[key] = val
    
    return idxDict

def _writeMandarinTeochewDict(filenameWithPath: str, pinyinChaoyinDict: Dict[str, Dict[str, str]], idxDict: Dict[str, List[int]]) -> Dict[str, List[int]]:
    *filePath, filename  = filenameWithPath.replace('\\', '/').rsplit('/', 1)
    filePath = filePath[0] if filePath else ''
    newIdxDict = {key:[] for key in idxDict}
    runningExtra = 0
    
    with open(filePath + '/' + filename, 'r', encoding='utf-8') as read_fp:
        with open(filePath + '/' + 'new_' + filename, 'w', encoding='utf-8') as write_fp:
            for line in read_fp:
                if line.startswith('#'):
                    write_fp.write(line)
                else:
                    newLine, extraCharCnt = addTeochewPronunciation(line, pinyinChaoyinDict)
                    tradChar, simpChar, *rest = newLine.split()
                    
                    idxDict, newIdxDict = updateIdxDict(tradChar, idxDict, newIdxDict, runningExtra)
                    
                    if tradChar != simpChar:
                        idxDict, newIdxDict = updateIdxDict(simpChar, idxDict, newIdxDict, runningExtra)
                    
                    runningExtra += extraCharCnt
                    write_fp.write(newLine)
            
    return idxDictToString(newIdxDict)

def updateIdxDict(word: str, oldDict: Dict[str, List[int]], newDict: Dict[str, List[int]], runningExtraCnt: int) -> (Dict[str, List[int]], Dict[str, List[int]]):
    idxList = oldDict[word]
                
    if len(idxList) > 1:
        idx = idxList.pop(0)
    else:
        idx, = oldDict.pop(word, None)
                
    idx += runningExtraCnt
    newDict[word].append(idx)

    return (oldDict, newDict)

def idxDictToString(idxDict: Dict[str, List[int]]) -> str:
    idxStringBuilder = []

    for key, idxList in idxDict.items():
        idxStringBuilder.append(key + ',' + ','.join([str(idx) for idx in idxList]) + '\n')
    
    return ''.join(idxStringBuilder)

if __name__ == '__main__':
    with open(MANDARIN_TEOCHEW_JSON_PATH + 'mandarin_teochew.json', 'r', encoding='utf-8') as f:
        pinyinChaoyinDict = json.load(f)
    
    idxDict = _readIdxToDict(IDX_DICT_PATH + 'cedict.idx')
    newIdxDictString = _writeMandarinTeochewDict(MANDARIN_TEOCHEW_DICT_PATH + 'cedict_ts.u8', pinyinChaoyinDict, idxDict)
    _writeDictToIdx(IDX_DICT_PATH + 'new_cedict.idx', newIdxDictString)
