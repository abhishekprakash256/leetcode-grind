"""
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.
"""

"""

Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
Example 2:

Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.
Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".

Constraints:

1 <= chars.length <= 2000
chars[i] is a lowercase English letter, uppercase English letter, digit, or symbol.

"""


"""

approach -- 

constraint case 

if len(chars) == 1 :

    return chars


modify in the place 

use two pointer like a sliding window ? 

["a","a","b","b","c","c","c"]

0 , 1 , 2 , 3, 4 , 5 , 6 , 7 

["a","2","b","2","c","3"]

r and slide l 

remove index ? 

imp case is r - l = 1 

nums[r] = 2 

r += 2 
l += 1 

count the length 

pop will work 


"""

from typing import List

class Solution:
    """
    passes leetcode
    """
    def compress(self, chars: List[str]) -> int:
        """
        Compress the character list in-place and return the new length.
        """

        # Pointer for writing the compressed characters
        write = 0  
        # Pointer for reading characters
        read = 0  

        while read <= len(chars) - 1 :
            
            char = chars[read]  # Current character
            count = 0  # Count occurrences

            # Count occurrences of the character
            while read <= len(chars) - 1  and chars[read] == char:
                read += 1
                count += 1

            # Write the character
            chars[write] = char
            write += 1

            # If count > 1, write the count as characters
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write  # New length of the compressed list




chars = ["a","a","b","b","c","c","c"]


sol = Solution()

print(sol.compress(chars))

print(chars)


                






