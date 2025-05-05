
input = ["bat", "tab", "tap", "pat", "cat"]

def group_anagrams(words: list[str]) -> list[list[str]]:

    keys = {}
    for word in words:
        w_s = tuple(sorted(word))
        if w_s not in keys:
            keys[w_s] = [word]
        else:
            keys[w_s].append(word)

    return [words for words in keys.values()]

print(group_anagrams(input))
