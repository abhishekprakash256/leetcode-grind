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



class Solution():
    """
    passes leetcode
    """


    def longest_palindromic_subsequence(self,s):

        n = len(s)
        dp = [[0] * n for _ in range(n)]
        
        # Every single character is a palindrome of length 1
        for i in range(n):
            
            dp[i][i] = 1
        
        # Check substrings of increasing lengths
        for length in range(2, n + 1):  # length varies from 2 to n

            for i in range(n - length + 1):

                j = i + length - 1  # endpoint of the substring
                
                if s[i] == s[j]:  # If first and last characters match

                    dp[i][j] = 2 + dp[i + 1][j - 1]

                else:  # Else, we consider the best of either removing left or right character
                    
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        
        return dp[0][n - 1]  # LPS of the entire string


    def isValidPalindrome(self,s, k):

        lps_length = self.longest_palindromic_subsequence(s)
        
        min_deletions = len(s) - lps_length

        return min_deletions <= k


