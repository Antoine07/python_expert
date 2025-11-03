c, m, w = 0, 0, ""  # utilisation des tuples unpackting pour assignation

with open('words.txt', 'r') as f:
    for l in f:
        word = l.strip()
        if len(word) > m:
            m, w = len(word), word
        c += 1

print(f"Nombre de ligne {c} - Le mot le plus long est: {w} ")