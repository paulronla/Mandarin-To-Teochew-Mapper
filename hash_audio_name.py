import os
import json

CHAOYIN_AUDIO_DICT_PATH = './'
BACKEND_PATH = '../../backend_teochew/Teochew-Dictionary-backend/' #where audio files are stored
IDX_NUM_DIGITS = 4 #number 
combined_chaoyin_audio_map = {}

with open(CHAOYIN_AUDIO_DICT_PATH 
        + 'chaoyin_audio.json', 'r', encoding='utf-8') as f:
    audio_hashes = json.load(f)

with open(CHAOYIN_AUDIO_DICT_PATH 
        + 'chaoyin_audio_map.json', 'r', encoding='utf-8') as f:
    audio_idxs = json.load(f)

for chaoyin, idx in audio_idxs.items():
    if chaoyin in audio_hashes:
        audio_hash = audio_hashes[chaoyin][0:8]
        new_filename = idx.zfill(IDX_NUM_DIGITS) + '_' + audio_hash
    else:
        new_filename = idx.zfill(IDX_NUM_DIGITS)

    os.rename(BACKEND_PATH + 'public/audio/c' + idx + '.mp3', 
            BACKEND_PATH + 'public/audio/' + new_filename + '.mp3')

    combined_chaoyin_audio_map[chaoyin] = new_filename

with open(BACKEND_PATH 
        + 'data/chaoyin_audio_map.json', 'w', encoding='utf-8') as f:
    json.dump(combined_chaoyin_audio_map, f, indent=4, ensure_ascii=False)
