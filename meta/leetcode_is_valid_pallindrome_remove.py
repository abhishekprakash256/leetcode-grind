"""
Given a string s and an integer k, return true if s is a k-palindrome.

A string is k-palindrome if it can be transformed into a palindrome by removing at
 most k characters from it.

 
"""

"""

Example 1:

Input: s = "abcdeca", k = 2
Output: true
Explanation: Remove 'b' and 'e' characters.
Example 2:

Input: s = "abbababa", k = 1
Output: true


Constraints:

1 <= s.length <= 1000
s consists of only lowercase English letters.
1 <= k <= s.length


"""


"""

approach -- 

how can we break the problem even ? 

abcdeca


if one element how much chnage ? 

if two elemnt how much change ? 

if 3 element how much change ? 

till nth element how much change ? 

n = len(nums) - 1 

we create a n X n matrix and put the data

abcb , remove 1 gets pallindrome , remove a

[[a],[ab],[abc],[abcb]]











"""