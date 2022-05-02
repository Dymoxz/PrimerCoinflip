import json

tempSeq = ['1.0', '2.0', '3.0', '4.0', '4.1']

with open('data.json', 'r+') as f:
    data = json.load(f)
    List = data["Cheater"]
    if tempSeq not in List:
        List.append(tempSeq)
    data["Cheater"] = List
    f.seek(0)
    json.dump(data, f, indent=4)
    f.truncate()