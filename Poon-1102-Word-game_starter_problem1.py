#Callaborate with Chuck

import random
import string

WORDLIST_FILENAME = "word_list.txt"


def secret_word():
    print("Reading word_list file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # word_list: list of strings
    word_list = line.split()
    return random.choice(word_list)

secret = secret_word()

def is_word_guessed(secret_word, letters_guessed):
    # FILL IN YOUR CODE HERE...
    counter = 0
    for character in secret_word:
        if character in letters_guessed:
            counter += 1
    if counter == len(secret_word):
        return True
    else:
        return False
    pass

print(secret)
print(is_word_guessed(secret, ["a", "b" "c", "d"]))





