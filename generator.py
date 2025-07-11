def collect_inputs(name, dob, pet):
    parts = []
    if name: parts.append(name)
    if dob: parts.append(dob.replace("-", ""))
    if pet: parts.append(pet)
    return parts

def apply_leetspeak(word):
    leet_map = {'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '$'}
    return ''.join(leet_map.get(c.lower(), c) for c in word)

def generate_variations(words):
    years = ['2023', '2024', '2025', '123', '1234']
    variations = set()

    for word in words:
        variations.add(word)
        variations.add(word.lower())
        variations.add(apply_leetspeak(word))
        for year in years:
            variations.add(word + year)
            variations.add(year + word)
            variations.add(apply_leetspeak(word) + year)

    return sorted(variations)

def save_wordlist(wordlist, filename="wordlist_output.txt"):
    with open(filename, "w") as f:
        for word in wordlist:
            f.write(word + "\n")
