
def get_first_duplicate(input: str):
    seen = set()

    for i in input:
        if i in seen:
            return i
        seen.add(i)

    return None

print(get_first_duplicate('aabbcddex'))
print(get_first_duplicate('abbcddex'))
print(get_first_duplicate('abcdex'))