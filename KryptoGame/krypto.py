"""

Simple Krypto generator

This program follows the rules provided by NCTM Illuminations 
    website link: chrome-extension://oemmndcbldboiebfnladdacbdfmadadm/https://illuminations.nctm.org/uploadedfiles/content/lessons/resources/3-5/krypto-as-rules.pdf

"""


import random

print("\n-------Krypto random number generator-------")

while True:
    krypto_possibilities = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10,
                            11, 11, 12, 12, 13, 13, 14, 14, 15, 15, 16, 16, 17, 17, 18, 19, 20, 21, 22, 23, 24, 25]
    krypto_list = []
    while len(krypto_list) < 6:
        krypto = random.choice(krypto_possibilities) # finds a random number in the list
        krypto_possibilities.remove(krypto) # removes the number from the list
        krypto_list.append(str(krypto))
    print(f"\nPlaying cards: {','.join(krypto_list[:5])}")
    print(f"Target card: {krypto_list[5]}")

    repeat = input("\nPlay again? (y/n) ")
    if repeat == 'n':
        break
