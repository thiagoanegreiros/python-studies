entry = ["ate", "eat", "tea", "bat", "tab", "tan", "nat"]

mydict = { }

for e in entry:
    key = tuple(sorted(e))
    if key in mydict:
        mydict[key].append(e)
    else:
        mydict[key] = [e]

result = [item for _, item in mydict.items()]
print(result)