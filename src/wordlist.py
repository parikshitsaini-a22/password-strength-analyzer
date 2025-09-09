def leetspeak(word):
    table = str.maketrans("aeios", "43105")
    return word.translate(table)

def generate_wordlist(name: str, pet: str, years: str):
    words = set()
    base_words = [name, pet, name+pet, pet+name]

    for w in base_words:
        if w:
            words.add(w)
            words.add(leetspeak(w))

    if years and "-" in years:
        start, end = map(int, years.split("-"))
        for y in range(start, end+1):
            for w in list(words):
                words.add(w+str(y))

    return sorted(words)
