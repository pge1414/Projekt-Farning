import json
import duden
import time, tqdm
from collections import deque

anzahlen = {}
wörter = []

with open('found_words.json', 'r') as f:
    for line in tqdm.tqdm(f, desc="Datei wird gelesen"):
        for i in json.loads(line).values():
            wörter.append(i)


flat_list = [item for sublist in wörter for item in tqdm.tqdm(sublist, desc="Flache Liste wird erstellt")]
flat_list = [item.lower() for item in flat_list]
anzahlen = {i: flat_list.count(i) for i in tqdm.tqdm(set(flat_list), desc="Anzahlen werden berechnet")}

anzahlen = dict(sorted(anzahlen.items(), key=lambda item: item[1]))
letzte_elemente = deque(anzahlen.items(), maxlen=86)
anzahlen = dict(letzte_elemente)
print(anzahlen)
print(len(anzahlen))
for word in tqdm.tqdm(anzahlen.keys(), desc="Verarbeitung läuft"):
    if duden.get(word) is not None:
        synonyme = duden.get(word).synonyms
        if synonyme:
            for synonym in synonyme:
                if synonym in flat_list:
                    anzahlen[word] += anzahlen[synonym]
                    anzahlen.remove(synonym)
                    time.sleep(0.1)
print(anzahlen)
print(len(anzahlen))
print(max(anzahlen, key=anzahlen.get))