from collections import Counter

text = "Python é ótimo. Python é simples! Python, simples e poderoso."

mylist = text.lower().replace('.', '').replace('!', '').replace(',', '').split()

countItems = { }

for item in mylist:
    if item in countItems:
        countItems[item] += 1
    else:
        countItems[item] = 1

top3 = sorted(countItems.items(), key=lambda x: x[1], reverse=True)[:3]
result = [word for word, _ in top3]

words = Counter(mylist).most_common(3)
newTop3 = [word for word, _ in words]

assert ["python", "é", "simples"] == result
assert ["python", "é", "simples"] == newTop3