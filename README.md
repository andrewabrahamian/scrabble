## Scrabble Solver in Python

Write a Python program that takes a Scrabble rack as a function argument and prints all "valid Scrabble English" words that can be constructed from that rack, along with their Scrabble scores, sorted by score.

Below are the requirements for the program:
- This needs to be able to be run as a function as shown below (not an input statement!)
- Name the python file: `scrabble.py` with the main function inside `scrabble.py` named `run_scrabble`
- Make a separate module named `wordscore.py` which contains, at a minimum, a function called `score_word`. This `score_word` function will take each word and return the score (scoring dictionary is described below). Import this function into your main `scrabble.py` program. 
- Allow anywhere from 2-7 character tiles (letters A-Z, upper or lower case) to be inputted. 
- Do not restrict the number of same tiles (e.g., a user is allowed to input ZZZZZQQ).
- Return two items from the `run_scrabble` function:
  - 1) The **total** list of valid Scrabble words that can be constructed from the rack as (score, word) tuples, sorted by the score and then by the word alphabetically as shown in the first example below. All outputted words need to be in upper case.
  - 2) The Total number of valid words as an integer
  - See examples below for the required output. The autograder is looking for this output so please make sure your solution is in the same format shown.
- You need to handle input errors from the user and suggest what that error might be caused by and how to fix it (i.e., a helpful error message). Return this error message as a string from the run_scrabble function (do not raise an exception).
- Implement wildcards as either `*` or `?`. There can be a total of **only** two wild cards in any user input (that is, one of each character: one `*` and one `?`). Only use the `*` and `?` as wildcard characters. A wildcard character can take any value A-Z. Replace the wildcard symbol with the letter in your answer (see the second example below). 
  - Wildcard characters are scored as 0 points, just like in the real Scrabble game. A word that just consists of two wildcards can be made, should be outputted and scored as 0 points. 
  - In a wildcard case where the same word can be made with or without the wildcard, display the highest score. For example: given the input 'I?F', the word 'if' can be made with the wildcard '?F' as well as the letters 'IF'. Since using the letters 'IF' scores higher, display that score.
- For partial credit, your program should take less than one minute to run with 2 wildcards in the input. For full credit, the program needs to run with 2 wildcards in less than 30 seconds.
- Write docstrings for the functions and puts comments in your code.
- You may only use the Python standard library in this assignment. However, any function in the standard library is allowed.
