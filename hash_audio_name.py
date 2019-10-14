import os
import json

BACKEND_PATH = '../../backend_teochew/Teochew-Dictionary-backend/'
IDX_NUM_DIGITS = 4
combined_chaoyin_audio_map = {}

with open('chaoyin_audio.json', 'r', encoding='utf-8') as f:
    audio_hashes = json.load(f)

with open('chaoyin_audio_map.json', 'r', encoding='utf-8') as f:
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

with open(BACKEND_PATH + 'data/chaoyin_audio_map.json', 'w', encoding='utf-8') as f:
    json.dump(combined_chaoyin_audio_map, f, indent=4, ensure_ascii=False)
