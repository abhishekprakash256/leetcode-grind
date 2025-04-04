"""
Implement a document scanning function wordCountEngine, which receives a string document
and returns a list of all unique words in it and their number of occurrences, sorted 
by the number of occurrences in a descending order. If two or more words have the same 
count, they should be sorted according to their order in the original sentence. 
Assume that all letters are in english alphabet. You function should be case-insensitive, so for instance, the words “Perfect” and “perfect” should be considered the same word.

The engine should strip out punctuation (even in the middle of a word) and use 
whitespaces to separate words.

Analyze the time and space complexities of your solution. Try to optimize for time
 while keeping a polynomial space complexity.
"""

"""

input:  document = "Practice makes perfect. you'll only
                    get Perfect by practice. just practice!"

output: [ ["practice", "3"], ["perfect", "2"],
          ["makes", "1"], ["youll", "1"], ["only", "1"], 
          ["get", "1"], ["by", "1"], ["just", "1"] ]

"""

"""
approach use a word list 

and then make a dict by iteration

how can I make a string to list

and then make a dict 



"""

import re

document = "Practice makes perfect. you'll only get Perfect by practice. just practice!"

document = re.sub(r'[^a-zA-Z0-9]', ' ', document)
new_doc = document.lower().split()

print(new_doc)

