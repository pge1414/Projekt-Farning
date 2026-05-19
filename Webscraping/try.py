import json

a=10
b=20
c=30
s = f"{a}-{b}-{c}"
print(s)
for i in range(3):
    print(i*7)
k = {"a": 1, "b": 2, "c": 3}
wörter = []

for i in k.values():
    wörter.append(i)
print(wörter)

with open("indexe.json", "r") as f:
    print(f.read())
    # data = json.load(f)
    # for i in data.values():
    #     wörter.append(i)