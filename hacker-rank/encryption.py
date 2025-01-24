"""
An English text needs to be encrypted using the following encryption scheme.
First, the spaces are removed from the text. Let  be the length of this text.
Then, characters are written into a grid, whose rows and columns have the following 
constraints:
"""

"""
count the number of chars after the strip of the text

square_root of L (with ceil function) <= row <= col 

find the square_root and put the ceril function  

get the numnber of rows 


result = []

s = s.strip()

length = len(s)

rows = ceil(sqrt(length))



"""


import math

def encryption(s):
    """
    Encrypts the input string using the described grid-based encryption scheme.

    :param s: A string to encrypt
    :return: The encrypted string
    passes code 
    """

    # Step 1: Remove spaces from the input string
    s = s.replace(" ", "")
    length = len(s)

    # Step 2: Determine the dimensions of the grid
    rows = math.floor(math.sqrt(length))
    cols = math.ceil(math.sqrt(length))
    
    # Ensure the grid area can accommodate all characters
    if rows * cols < length:
        rows += 1

    # Step 3: Create the grid
    grid = [s[i:i + cols] for i in range(0, length, cols)]

    # Step 4: Read columns to generate the encoded message
    encrypted_message = []
    for col in range(cols):
        column_text = "".join(row[col] for row in grid if col < len(row))
        encrypted_message.append(column_text)
    
    # Step 5: Combine the columns with spaces
    return " ".join(encrypted_message)

