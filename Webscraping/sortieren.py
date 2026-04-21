import json

anzahlen = {}
wörter = []

with open('found_words.json', 'r') as f:
    for line in f:
        for i in json.loads(line).values():
            wörter.append(i)

flat_list = [item for sublist in wörter for item in sublist]
anzahlen = {i: flat_list.count(i) for i in set(flat_list)}
anzahlen = dict(sorted(anzahlen.items(), key=lambda item: item[1]))
print(anzahlen)
print(max(anzahlen, key=anzahlen.get))