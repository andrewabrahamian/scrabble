# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 12:44:06 2022

@author: andre
"""

def score_word(word, rack, rack_letters):
    '''Take a word and calculate its score based on letter values'''
    scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
          "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
          "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
          "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
          "x": 8, "z": 10}
    scores["?"] = 0
    scores["*"] = 0
# =============================================================================
#     scores["?"] = 0
#     scores["*"] = 0
#     
#     total = 0
#     
#     for letter in word:
#         total += scores[letter]
#     return [total, word]
# 
# =============================================================================
    
    total = 0
    if "?" in rack or "*" in rack:
        for letter in rack:
            if letter not in rack_letters:
                total += scores[letter]
                #if letter in "*?":
                #    scores[letter] = 0
                #else:
                #    total = total + scores[letter]
                
                #try:
                #    total = total + scores[letter]
                #except KeyError:
                #    pass
        return [total, word]
    else: 
        for letter in word:
            total += scores[letter]
        return [total, word]
