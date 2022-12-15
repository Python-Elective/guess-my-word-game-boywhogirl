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
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
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

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    output = ""
    for character in secret_word:
        if character in letters_guessed:
            output += character
        else:
            output += ""
    return output
    pass

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    letters = ""
    for character in string.ascii_lowercase:
        if character not in letters_guessed:
            letters += character
    return letters
    pass

print(secret)
print(get_available_letters(['f', 'g','h','e','a']))





