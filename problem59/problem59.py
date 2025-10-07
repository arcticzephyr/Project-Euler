import os
from collections import defaultdict

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "0059_cipher.txt")
with open(file_path, "r") as f:
    encrypted_text = f.read()
    encrypted_text = encrypted_text.split(',')
    most_common_letter = max(set(encrypted_text), key=encrypted_text.count)
    keymap = defaultdict(int)
    test_word = [ord(x) for x in " th"]

    for i in range(len(encrypted_text) // 3):
        current_block = encrypted_text[3*i:3*i+3]
        keymap[tuple(test_word[j]^int(current_block[j]) for j in range(3))] += 1

    best = max(keymap, key=keymap.get)
    print(best)
    text = encrypted_text.copy()

    for i in range(0, len(encrypted_text), 3):
        for j in range(3):
            if i + j < len(encrypted_text):
                text[i + j] = best[j] ^ int(encrypted_text[i + j])

    
    print(sum(text))
