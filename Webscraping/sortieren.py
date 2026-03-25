import json

anzahlen = {}
wörter = {}

with open("found_words.json", "r") as f:
    wörter = json.load(f)

for i in wörter.values():
    i.sort()
    for j in i:
        if line.strip()
        anzahlen[j] = anzahlen.get(j, 0) + 1

print(anzahlen)