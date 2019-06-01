import json

teochewDict = {
	"一": {
		"yi1": "zêg8|ig4|iao1"
	},
	"弹": {
		"dan4": "tang5",
		"tan2": "tang5|duan7"
	}
}

with open('teochewDict.json', 'w', encoding='utf-8') as f:
    json.dump(teochewDict, f, ensure_ascii=False, indent=4)

with open('teochewDict.json', 'r', encoding='utf-8') as f:
    teochewDict = json.load(f)

print(teochewDict['弹']['tan2'])

