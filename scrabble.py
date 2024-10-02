# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 12:14:17 2022

@author: andre
"""
# import score_word from wordscore module
from wordscore import score_word

# =============================================================================
# scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
#           "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
#           "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
#           "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
#           "x": 8, "z": 10}
# =============================================================================

# import scrabble words as list of words
with open("sowpods.txt","r") as infile:
    raw_input = infile.readlines()
    data = [datum.strip('\n') for datum in raw_input]
    
def run_scrabble(word):
    '''
    Function takes rack of between 2 and 7 scrabble letters, and
    calculates the possible number and scores of words that can be played 
    from that combination.
    '''
    
    # Error Checking + Print Sections
    if type(word) != str:
        print("must play a word")
        return "You must play a word!"
    # length of word is shorter than two or longer than seven letters
    elif len(word) < 2 or len(word) > 7:
        print("must play a word of correct length")
        return "You must play between two and seven letters!"
    # more than one wildcard of each type is played
    elif word.count("*") > 1 or word.count("?") > 1:
        print("must play correct # of wildcards")
        return "You must only play one type of each wildcard!"
    # a user inputs a number
    elif word.isdigit():
        print("must play letters and wildcards")
        return "You must only play valid characters!"
    # a user inputs an otherwise invalid character
    for char in word:
        if char in "1234567890!#$%&'()+,-./:;<=>@[\]^_`{|}~": #remove our wildcards
            print("must play valid letters and wildcards")
            return "You must only play valid characters and wildcards!"
        continue
    
    rack = word
    rack_low = rack.lower()
    
    valid_words = []
    
    for word in data:
        word_low = word.lower()
        candidate = True
        rack_letters = list(rack_low)
        for letter in word_low: #have to embed wildcard check here
            if letter in rack_letters:
                rack_letters.remove(letter)
            elif '*' in rack_letters:
                rack_letters.remove("*")
            elif '?' in rack_letters:
                rack_letters.remove("?")    
            else:
                candidate = False
        
        if candidate:    
            # Get the Scrabble scores for each word.
            valid_words.append(score_word(word_low, rack_low, rack_letters))
    
    # Print the valid words, sorted by Scrabble score.
    
    valid_word_list = []
    
    valid_words.sort(key = lambda x: (x[0]), reverse = True)
    
    for entry in valid_words:
        valid_word_list.append((entry[0], entry[1].upper()))
    
    print((valid_word_list, len(valid_words)))
    return (valid_word_list, len(valid_words))

run_scrabble("PEN*?in")

#rack = "ZAEfiee"
#rack = "?*f"
#rack = "ZZZZEE"
#rack = "PEN*?in"