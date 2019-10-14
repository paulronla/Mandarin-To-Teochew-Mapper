# Mandarin-To-Teochew-Mapper
For every Chinese character, maps the Mandarin pronunciation to Teochew pronunciation. 
This is accomplished through the below scripts, merging 
[CC-CEDICT](https://cc-cedict.org) \(public-domain Chinese-English dictionary\) 
and the [Teochew Phoneme Dictionary](http://www.czyzd.com), producing a 
a much needed Teochew-Chinese-English dictionary to be used by Teochew applications.

## What is Teochew?
[Teochew](https://en.wikipedia.org/wiki/Teochew_dialect) is a dialect of 
Chinese with over 25 million speakers worldwide. Outside of China, it is 
among one of the most spoken Chinese varieties only surpassed by 
Mandarin, Cantonese, and Taiwanese/Hokkien. Phonetically, it has not 
changed very much and many vocabularies from Japanese, Korean, and Vietnamese 
that originated from China centuries ago still sound similar.

For example, consider 肉 which means flesh. \[Niku\] is one of the common 
Japanese readings borrowed from China along with the character. Compare with 
Teochew \[nek8\] \([POJ spelling](https://en.wikipedia.org/wiki/Pe̍h-ōe-jī)\) 
and Mandarin \[rou4\].

## Generate the Teochew-Chinese-English dictionary
The dictionary is generated in two steps. First generate ```mandarin_teochew.json```, 
which provides the Mandarin to Teochew pronunciation mapping per Chinese character. 
```mandarin_teochew.json``` is then used to do the look up per Chinese word \(which 
can contain multiple Chinese characters\), generating all of the Teochew needed for a 
full Chinese dictionary.

### Execute ```build_teochew_json.py```
The script converts HTML scraped from the Teochew Phoneme Dictionary containing entries 
for over 9000 Chinese characters. HTML can be fetched using 
[Teochew-Dictionary-Scraper](https://github.com/paulronla/Teochew-Dictionary-Scraper). 
The ```TEOCHEW_HTML_PATH``` needs to contain the HTML. Update constants as needed:

```python
TEOCHEW_HTML_PATH = '../../teochew_dict_html/'
OUTPUT_DIR = './'
START_PAGE = 0
END_PAGE = 916
```

### Execute ```build_mandarin_teochew_dict.py```
This script requires ```mandarin_teochew.json``` from the previous script and the 
CC-CEDICT file named ```cedict_ts.u8``` and the corresponding index file 
```cedict.idx```. Update constants as needed:

```python
MANDARIN_TEOCHEW_JSON_PATH = ''
IDX_DICT_PATH = ''
MANDARIN_TEOCHEW_DICT_PATH = ''
```

```new_cedict_ts.u8``` and ```new_cedict.idx``` will be created reflecting the Teochew 
pronunciation additions

## Map Teochew pronunciations to hashed Teochew audio file names

In order to prevent scraping of Teochew audio from the back end API, ```hash_audio_name.py``` 
grabs the old filenames from ```chaoyin_audio_map.json``` and appends them with a hash to 
make brute force guessing too time consuming. The script also generates a new JSON with 
Teochew pronunciations as the key and the corresponding pronunciation mp3 as the value. The 
resulting file is used directly in 
[Teochew-Dictionary-Backend](https://github.com/paulronla/teochew-dictionary-backend).