

def mergeAlternately(word1: str, word2: str) -> str:
    min_length = min(len(word1), len(word2))
    result = []
    for w1, w2 in zip(word1, word2):
        result.append(w1)
        result.append(w2)

    result.append(word1[min_length:])
    result.append(word2[min_length:])

    return ''.join(result)

print(mergeAlternately('aaaa', 'bbbbbbb'))

range(10)
